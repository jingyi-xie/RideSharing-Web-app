# Ride Sharing Web-app

> This project is similar to **Uber**, the only difference is that **it's a web-app**!

### Functionalities:
* **Create Account** – A user should be able to create an account if they do not have one.
* **Login/Logout** – A user with an account should be able to login and logout.
* **Driver Registration** – A logged-in user should be able to register as a driver and enter their personal and vehicle info. They should also be able to access and edit their info.
* **Ride Selection** – If a logged-in user is part of multiple rides, she should be able to select which ride she wants to perform actions on.
* **Ride Requesting** – A logged-in user should be able to request a ride. Requesting a ride should allow the owner to specify the destination address, a required arrival date / time, the number of total passengers from their party, a vehicle type (optionally), whether the ride may be shared by other users or not, and any other special requests.
* **Ride Request Editing (Owner)** – A ride owner should be able to edit the specific requested attributes of the ride as long as the ride is not confirmed.
* **Ride Status Viewing (Owner / Sharer)** – A ride owner or sharer should be able to view the status of their non-complete rides. For open ride requests, this should show the current ride details (from the original request + any updates due to sharers joining the ride). For confirmed ride requests, the driver and vehicle details should also be shown.
* **Ride Status Viewing (Driver)** – A ride driver should be able to view the status of their confirmed rides, which should show the information for the owner and each sharer of the ride, including the number of passengers in each party. A driver should also be able to edit a ride to mark it as complete.
* **Ride Searching (Driver)** – A driver should be able to search for open ride requests. Only requests which fit within the driver’s vehicle capacity and match the vehicle type and special request info (if either of those were specified in the ride request) should be shown. A driver can claim and start a ride service, thus confirming it. Once closed, the ride owner and each sharer should be notified by email that the ride has been confirmed (hence no further changes are allowed).
* **Ride Searching (Sharer)** – A user should be able to search for open ride requests by specifying a destination, arrival window (the user’s earliest and latest acceptable arrival time) and number of passengers in their party. A sharer should be able to join a selected ride, if any exist in the resulting list of pending rides.
