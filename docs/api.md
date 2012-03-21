REST API Resources
=================


Timelines
-----------
Timelines are collections of Punns, ordered with the most recent first.


* GET punns/home_timeline
* GET punns/mentions
* GET punns/repunned_by_me
* GET punns/repunned_to_me
* GET punns/repunned_of_me
* GET punns/user_timeline
* GET punns/repunned_to_user
* GET punns/repunned_by_user


Punns
-----------
A Punn is either an image or a video associated with a caption and additional associated metadata. 

* GET punns/:id/repunned_by
* GET punns/:id/repunned_by/ids
* GET punns/repunns/:id
* GET punns/show/:id
* POST punns/destroy/:id
* POST punns/repunn/:id
* POST punns/update
* POST punns/update_with_media


Search
-----------
Find relevant Punns based on queries performed by your users.

* GET search

Friends & Followers
-----------
Users follow their interests on Twitter through both one-way and mutual following relationships.
