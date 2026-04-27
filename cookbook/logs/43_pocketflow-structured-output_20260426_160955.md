=== Resume Parser — Structured Output ===


=== STRUCTURED RESUME DATA ===

name: John Smith
email: johnsmtih1983@gnail.com
phone: (555) 123-4556
address: 123 Main st, Anytown, USA
summary: Dedicated and hardworking professional with over 10 years of exprience in
  business manegement. Known for finding creatve solutions to complex problems and
  excelent communication skills. Seeking new opportunites to leverage my expertise
  in a dynamic environment.
work_experience:
- title: SALES MANAGER
  company: ABC Corportaion
  dates: June 2018 - Present
  responsibilities:
  - Oversee a team of 12 sales represenatives and achieve quarterly targets
  - Increased departmnet revenue by 24% in fiscal year 2019-2020
  - Implemneted new CRM system that improved efficiency by 15%
  - Collabarate with Marketing team on product launch campaigns
  - Developed training materials for new hiers
- title: ASST. MANAGER
  company: XYZ Industries
  dates: March 2015 - May 2018
  responsibilities:
  - Assisted the Regional Manager in daily operations and reporting
  - managed inventory and vendor relations
  - Trained and mentored junior staff members
  - Recieved "Employee of the Month" award 4 times
- title: CUSTOMER SERVICE REPRESENTATIVE
  company: Fast Solutions Inc
  dates: January 2010 - February 2015
  responsibilities:
  - Responded to customer inquiries via phone email, and in-person
  - Resolved customer complaints and escalated issues when necessary
  - Maintained a 95% customer satsfaction rating
education:
- degree: Bachelor of Business Administration
  institution: University of Somewhere
  dates: 2006 - 2010
  gpa: 3.6/4.0
- degree: Associate Degree in Communications
  institution: Community College
  dates: 2004-2006
skills:
- Microsoft Office: Excel, Word, Powerpoint (Advanced)
- Customer relationship management (CRM) software
- Team leadership & managment
- Project management
- Public speaking
- Time managemant
references: Available upon request
other_activities:
- Volunteer at the local food bank (2016-present)
- Member of Toastmasters International
- Enjoy hiking and photografy
skill_indexes:
- 0: Team leadership & management
- 1: CRM software
- 2: Project management
- 3: Public speaking
- 4: Microsoft Office

✅ Extracted resume information.

--- Found Target Skills ---
Traceback (most recent call last):
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-structured-output/main.py", line 96, in <module>
    main()
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
    return callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-structured-output/main.py", line 84, in main
    if 0 <= idx < len(DEFAULT_SKILLS):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: '<=' not supported between instances of 'int' and 'dict'
