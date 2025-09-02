# Example Copilot Prompt for Java 1.8, Spring Boot, Spring REST, Spring Data JPA

```
Role: You are a senior Java backend engineer.
Task: Implement a REST API for managing products in an e-commerce application using Spring Boot 2.x, Spring REST, and Spring Data JPA.
Context: The project uses Java 1.8. The Product entity has fields: id (Long), name (String), price (BigDecimal), and description (String). Use an H2 in-memory database for persistence.
Process: 
- Create the Product entity.
- Create a Spring Data JPA repository for Product.
- Implement a REST controller with CRUD endpoints: GET /products, GET /products/{id}, POST /products, PUT /products/{id}, DELETE /products/{id}.
- Use standard Spring annotations and best practices.
Response: Provide the complete Java code for the entity, repository, and controller classes, ready to be used in a Spring Boot project.
```

## Example Java Entity Class

```java
package com.example.demo.model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import java.math.BigDecimal;

@Entity
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private BigDecimal price;
    private String description;

    // Constructors
    public Product() {}

    public Product(String name, BigDecimal price, String description) {
        this.name = name;
        this.price = price;
        this.description = description;
    }

    // Getters and setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public BigDecimal getPrice() { return price; }
    public void setPrice(BigDecimal price) { this.price = price; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
}
```
