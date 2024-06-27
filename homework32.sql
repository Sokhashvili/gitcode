CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    ContactName VARCHAR(100),
    Country VARCHAR(50)
);


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);


INSERT INTO Customers (CustomerID, CustomerName, ContactName, Country)
VALUES
(1, 'Giorgi Lomaia', 'Jaba Kankava', 'Georgia'),
(2, 'Cristiano Ronaldo', 'PEPE', 'Portugal'),
(3, 'Raul Gonzales', 'Fernando Torres', 'Spain');


INSERT INTO Orders (OrderID, OrderDate, CustomerID)
VALUES
(1, '2024-06-01', 1),
(2, '2024-06-02', 2),
(3, '2024-06-03', 3),
(4, '2024-06-04', 1);


SELECT * FROM Customers;


SELECT * FROM Orders;


SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerName
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID;