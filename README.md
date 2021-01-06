# Icetrack

Icetrack is a Python Django-based inventory management system created for CS 532 - Software Engineering. The web application, referred to as Icetrack, supports the following business functional areas: order entry, inventory management, shipment tracking, and issue ticket management. The front end of this inventory management system was built using Bootstrap with the [SB Admin 2 theme](https://github.com/startbootstrap/startbootstrap-sb-admin-2) as a foundation.

## Implementation

Django was chosen for the back end of this project because of its flexibility and minimal barrior to entry. The documentation and community support allowed for both a relatively simple setup and minimal time spent overcoming roadblocks. Class-based views were chosen over function-based views to make use of Django's built-in generic class-based views for even further acceleration at the start of the project.  

In order to allow for the most focus to be spent on building the back end of the project, Bootstrap was chosen for the front end. Using the SB Admin 2 theme as a starting point allowed for more time to be spent building and enhancing the back end of the project which was the focal point for this project.

## Authentication

The Icetrack inventory management system has three levels of authentication: non-registered users, registered users, and administrators. The visibility and functionality of the components outlined below is entirely dependant on the user's level of authentication. Non-registered users are not allowed access to the application and are redirected to the login page from anywhere they attempt to access. Registered users are given minimal access to the orders and tickets components. Administrators are given full access to the system and shown additional insights on the dashboard.  

The Icetrack system leverages Django's built-in registration and authentication system with simple Bootstrap components layered over it for the front end. Users can register a new account or login with/reset password for an existing account.

## Components

There are five main components in the Icetrack inventory management system: home, inventory, orders, shipments, and tickets. For the sake of keeping this readme concise, not all pages are outlined here. In additiona to the overview pages, each component has additional pages for viewing item details (see \*_detail.html templates) and creating/updating an item (see create_/*.html templates).

### Home

**Template**: home.html  
**View**: HomePageView

#### Registered User

A registered user lands on the welcome page where they can use the navigation menu to create or view their orders/tickets.

![Registered user home page](https://i.postimg.cc/W1Cw3gY7/home-regu.png)

#### Administrator

An administrator lands on the dashboard which gives an overview of all components of the system along with a few charts to provide a snapshot of sales and inventory data.

![Administrator home page](https://i.postimg.cc/fRDJvLth/home-admin.png)

### Inventory

**Template**: inventory.html  
**View**: InventoryPageView

#### Administrator

To protect the integrity of the inventory system, only administrators are able to access the all inventory page. This page provides details about the items in the inventory along with functionality to create, read, update, and delete inventory items as needed as well as open tickets for any issues with the inventory component.

![Inventory page](https://i.postimg.cc/0yXPJ27n/inventory-admin.png)

### Orders

**Template**: orders.html  
**View**: OrdersPageView

#### Registered User

Registered users are allowed access to see the orders they have created. From here, they have functionality to view order details, create a new order, or open a ticket for an encountered issue.

![Registered user orders page](https://i.postimg.cc/66PPR2Py/orders-regu.png)

#### Administrator

Administrators are allowed to see all orders placed and are given access to create orders, view order details, update orders, delete orders, and open tickets. 

![Administrator orders page](https://i.postimg.cc/WbJH7pRS/orders-admin.png)

### Shipments

**Template**: shipments.html  
**View**: ShipmentsPageView

#### Administrator

To protect the integrity of the inventory system, only administrators are able to access the all shipments page. This page shows details about the shipments created for orders along with functionality to create, read, update, and delete shipments as needed. Additionally, users can open tickets for any issues they came across in this component.

![Shipments page](https://i.postimg.cc/3r0stFmg/shipments-admin.png)

### Tickets

**Template**: tickets.html  
**View**: TicketsPageView

#### Registered User

Registered users are allowed access to see the tickets they have opened. From here, they have functionality to view ticket details or create a new ticket.

![Registered user tickets page](https://i.postimg.cc/ZYNQ8KzH/ticketss-regu.png)

#### Administrator

Administrators are allowed to see all tickets opened and are given access to create ticket, view ticket details, update ticket, and delete tickets. 

![Administrator tickets page](https://i.postimg.cc/7LbsfqNg/tickets-admin.png)


