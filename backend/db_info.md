## Database Information

### Product
    - Name
    - Image(s)
    - Price
    - Discount %
    - Stock Remaining 
    - ( Recommender System MetaData )
    - Size
        - Can be set by Admin
        - We’ll put a template of S, M, L
    - Description
    - Materials - list of strings
    - Weight
    - Dimension
    - Type of ( Pairs )
    - Reviews
    - Categories - Multiselect
        - Category - Enum 
  
### Review
    - Customer Name
    - Customer Image
    - Description
    - Rating - int
    - Image

### Product Listing
    - Product
    - Quantity
    - Listing Price
    - Coupon Discount
	
### Sales
    - Cart? -> Sale Item
    - Buyer Name?
    - Price
    - Verified - bool
        - 
    - If more than 10 orders, additional verification
        - After first 2 months of use
### Cart
    - Product Listing
    - Buyer Id (number? Name?)
    - Delivery Data
    - Paid - Paid, Failed, Pending

### Account
    - Name (optional)
    - Phone Number
        - Facebook (Instagram) Login
    - Sales History
    - Address (View Pick n Drop Nepal’s Requirement)
	
### SuperUser
    - (handled by Django)
	
### Employee
    - Name
    - Address
    - Role
        - Controlled by SuperAdmin (Admin, Manager, Sales)
        - Sales - Can accept/reject orders
        - Manager - Can Manage Employees