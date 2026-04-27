graph TD
    A[Code Push] --> B(Build);
    B --> C{Test & Lint (Parallel)};
    C --> D{Staging Deploy};
    D --> E[Manual Approval];
    E -- Approved --> F{Production Deploy};
    E -- Rejected --> G[Rollback to Build];