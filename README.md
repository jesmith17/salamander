# Project Salamander

![Original Salamander Cartoon](https://upload.wikimedia.org/wikipedia/commons/9/96/The_Gerry-Mander_Edit.png)


Project Salamander is an open source effort to leverage software and data to address the problem of political gerrymandering. 


## Concept

Combine geospatical data with population data to generate maps for state and federal elections that are fair, and are completely blind to race, polcitical party, and other partisan demographics. 


* Uses existing planimetric boundaries
  * State boundaries
  * County boundaries
  * City boundaries
  * School District boundaries
  * School attendance boundaries (High School -> Elementary)

 The concept is that by using these existing boundaries (where spliting of the smallest boundaries is completely forbidden) the project blocks many of the tactics used for gerrymandering today. 

 The project considers these points when suggesting maps. 

 * Total population of the district (target +- 2% of even distribution)
 * Contiguous boundaries (no disconnected areas)
 * Weighted Number of split boundaries (smaller boundaries like a high school attendance area) are given more weight, so splitting those is discouraged
 * Avg distance from the center of any district to all of its boundaries. (Boundaries should be both navigable and contigous).

**What the project does not consider**

* Political affiliation
* Race
* Gender
* Representative conflict ( maps shoudl be based on where the people are, not whether or not a change im map puts 2 elected officials in a situation to compete aginast each other in a district). 


## Status

I have started to add some basic structure including some early concepts of the logic. But the project is pre-Alpha at this point. 


## Contributing

Any one who wants to contribute to the project is encouraged to do so. Ideally the project needs people who are experienced in python, geospatial queries, and entropy models. 

Specifically the challenge that worries me most is how to make sure that the map it suggests is the right one.  Currently the system would use a greedy approach to boundaries, where the order in which it consumes the boundaries could create less optimal maps. So people with expertise in how to help address this, or how to score a maps viability, would be especially appreciated. 

