import click
from datetime import datetime, timedelta
from pocketflow import Flow
from nodes import CreateCalendarEventNode, ListCalendarEventsNode, ListCalendarsNode


def create_calendar_flow():
    """Creates a flow to manage calendar events."""
    create_event_node = CreateCalendarEventNode()
    list_events_node = ListCalendarEventsNode()
    create_event_node - "success" >> list_events_node
    create_event_node - "error" >> None
    return Flow(start=create_event_node)


def list_calendars_flow():
    """Creates a flow to list all user calendars."""
    return Flow(start=ListCalendarsNode())


@click.command()
@click.option("--summary", default="Example Meeting", show_default=True,
              help="Event title/summary")
@click.option("--description", default="An example meeting created by PocketFlow",
              show_default=True, help="Event description")
@click.option("--days-ahead", default=1, show_default=True,
              help="Number of days from now to schedule the event")
@click.option("--duration-hours", default=1, show_default=True,
              help="Duration of the event in hours")
@click.option("--list-only", is_flag=True, default=False,
              help="Only list calendars, do not create an event")
def main(summary, description, days_ahead, duration_hours, list_only):
    """Create and list Google Calendar events via PocketFlow."""
    click.echo("=== Listing your calendars ===")
    shared = {}
    list_calendars_flow().run(shared)
    if "available_calendars" in shared:
        for cal in shared["available_calendars"]:
            click.echo(f"  - {cal.get('summary')}")

    if list_only:
        return

    click.echo("\n=== Creating calendar event ===")
    start_time = datetime.now() + timedelta(days=days_ahead)
    end_time = start_time + timedelta(hours=duration_hours)

    shared = {
        "event_summary": summary,
        "event_description": description,
        "event_start_time": start_time,
        "event_end_time": end_time,
        "days_to_list": 7,
    }
    create_calendar_flow().run(shared)

    if "last_created_event" in shared:
        click.echo(f"Event created: {shared['last_created_event']['id']}")
    else:
        click.echo("Event creation may have failed — check logs above.")


if __name__ == "__main__":
    main()
