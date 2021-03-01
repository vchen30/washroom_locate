# WhereToWee Web Application

![Screenshot](https://github.com/vchen30/washroom_locate/blob/master/sample.PNG)

## How to run

First, run:

`vagrant up`

The website should be up and running on: http://localhost:8080/home/

## Login Info 

Username/Password:
* user1/user1 (superuser)


## Working Features

Map
* Displays washrooms throughout Metro Vancouver.
* Clicking on a washroom icon displays a popup containing its id, and links to the detail and review pages.
* Clicking on a washroom icon displays the driving directions from the user's current location to the washroom.
* Right clicking on the map updates the user location peg.

Filter
* Clicking on a arrow button on the right side of the page displays a sidebar with a filter and a list view of washrooms in the order of the nearest to farthest washrooms.
* Clicking on the filter items and then clicking on "Apply Filter" updates the map and the list view with washrooms that satisfy the filter criteria.
* The washroom list also displays opening hours for washrooms that had opening hour specified in the dataset.
* Clicking on a washroom opens a details page for that washroom.

Washroom Details
* Displays washroom details including rating, unisex, public access, water fountain, etc.
* Displays reviews.


Review System 
* Users can submit a review for a washroom by entering its rating (1-Terrible to 5-Excellent) and comment. 
* A submitted review is not posted until the administrator moderates its content for appropriateness and marks the in_public attribute of the review as True in the admins page. 
* Once in_public is set to True, the review can be viewed on the washroom details page. 
* In the washroom details page, the average rating gets updated according to the reviews.
 
 


## References

https://realpython.com/location-based-app-with-geodjango-tutorial/

Data was extracted from: 
http://www.openstreetmap.org/, https://overpass-turbo.eu/
