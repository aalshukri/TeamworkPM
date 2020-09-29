# TeamworkPM

The python script in this repository can be used to create summary statistics for projects on [TeamworkPM](https://www.teamwork.com/?partner=wd7z88gg5r). 

The script produces monthly reports which I am using to understand two main aspects:

1. The projects have we worked on

2. The ratio of time spent per task category (for each project)


This information can then be used to help:

- Project planning: understanding what project we have worked on vs what we planned to work on
- Understand the ratio of time spent on tasks within project
	ie, new features, bugs, email, meetings, etc  
- Reflect on what went well, what not went well
- Highlight areas of improvement



## Running instructions

`> docker build -t teamworkpm-app .`

`> docker run -it teamworkpm-app`
