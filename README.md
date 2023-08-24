# Photo Search
A simple program for those who have crazy file structures but still want to find their photos. Provided they named them something they can search with.

This is for someone that has a ton of photos and wants to consolidate them. 

The way it works is it takes the "First name" and uses this as a first search term. Then last name is uesd to filter the first search results 

Example "Jenny Birthday" would search for all files containing Jenny then would pass them to grep and filter for Birthday.
It would then copy all of those files to a local folder under "Jenny Birthday"

