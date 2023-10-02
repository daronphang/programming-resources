## Metadata Annotations

Developers use annotations to inform JPA which objects should be persisted, and how they should be persisted. The annotations are present in the javax.persistence package.

### @Entity

Informs JPA that the class and its objects should be persisted.

```java
@Entity
public class Musician {}
```

### @Table

Specifies the table in the database with which the entity is mapped.

```java
@Entity
@Table(name = "employee")
public class Employee implements Serializable {}
```

### @Column

Specifies the column mapping.

```java
@Entity
@Table(name = "employee")
public class Employee implements Serializable {

  @Column(name = "employee_name")
  private String employeeName;
}
```

### @Id

Specifies the primary key of the entity.

```java
@Entity
@Table(name = "employee")
public class Employee implements Serializable {
  @Id
  @Column(name = "id")
  private int id;
}
```

### @GeneratedValue

Specifies the generation strategies for the values of primary keys.

### @OrderBy

For sorting of data.

### @Transient

Every non-static and non-transient property of an entity is considered persistent, unless it is annotated with @Transient.

```java
@Transient
Private int employeePhone;
```

## Entity Relationships (Mapping between Tables)

### @OneToOne, @PrimaryKeyJoinColumn

Used for associated entities sharing the same primary key.

```java
@Entity
@Table(name = "employee")
public class Employee implements Serializable {

  @Id
  @Column(name = "id")
  @GeneratedValue
  private int id;

  @OneToOne(cascade = CascadeType.MERGE)
  @PrimaryKeyJoinColumn
  private EmployeeDetail employeeDetail;
}

@Entity
@Table(name = "employeeDetail")
public class EmployeeDetail implements Serializable {

  @Id
  @Column(name = "id")
  private int id;
}
```

### @OneToOne, @ManyToOne, @OneToMany, @ManyToMany, @JoinColumn

Used when foreign key is held by one of the entities.
