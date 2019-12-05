# Data_Wrangling
Week 1 - Python Basics and Files <br>
Week 2 - Working with Excel files <br>
Week 3 - PDFs <br>
Week 4 - Databases - SQL and NoSQL<br>
Week 5 - Data cleaning, formatting, standardizing, and investigation<br>
Week 6 - Exploratory Data Analysis and Visualization<br>
<ul>
	<li> Matplotlib - Magic </li>
	<li> Seaborn - pair plots, Categorical plot, Pivot tables, Heatmap</li>
	<li>  Altair - Tidy Data, chart objects (marks and Encoding),Aggregation, Compound charts(layering, HConcat and VConcat)</li>
	<li>  Bonus -- Creating a Dashboard with Altair and Panel</li>
</ul>
Week 7 - <br>
Week 8 - <br>


Git Large File Storage<br>
Git Large File Storage (LFS) replaces large files with text pointer inside Git while sotreing the files contents on a remote server like GitHub.com<br>
1. Once per repositiory set up Git LFS and its hooks by running<br>
<ul>
<li> git lfs install </li>
</ul>
2-a. Select the file types you'd like Git LFS to manage
<ul>
<li> git lfs track "*.ext" </li>
</ul>
2-b. Make sure .gitattributes is tracked
<ul> 
<li> git add .gitattributes </li>
</ul>
3. Commit and push to GitHub as Normal
<ul> 
<li> git add file.ext </li>
<li> git commit -m "Add design file" </li>
<li> git push origin master </li>
</ul>
