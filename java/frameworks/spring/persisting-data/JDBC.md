## JdbcTemplate

Spring JDBC support is rooted in the JdbcTemplate class which provides a means by which developers can perform SQL operations against a relational database, without all the boilerpalte typically required when working with JDBC.

### Adding Dependency

Requires a database where your data will be stored.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId>
</dependency>
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

### Without JdbcTemplate

```java
@Override
public Ingredient findOne(String id) {
    Connection connection = null;
    PreparedStatement statement = null;
    ResultSet resultSet = null;

    try {
        connection = dataSource.getConnection();
        statement = connection.prepareStatement(
        "select id, name, type from Ingredient");
        statement.setString(1, id);
        resultSet = statement.executeQuery();
        Ingredient ingredient = null;
        if(resultSet.next()) {
            ingredient = new Ingredient(
            resultSet.getString("id"),
            resultSet.getString("name"),
            Ingredient.Type.valueOf(resultSet.getString("type")));
        }
        return ingredient;
    } catch (SQLException e) {
        // ??? What should be done here ???
    } finally {
        if (resultSet != null) {
            try {
                resultSet.close();
            } catch (SQLException e) {}
        }
        if (statement != null) {
            try {
                statement.close();
            } catch (SQLException e) {}
        }
        if (connection != null) {
            try {
                connection.close();
            } catch (SQLException e) {}
        }
    }
    return null;
}
```

### With JdbcTemplate

```java
private JdbcTemplate jdbc;
@Override
public Ingredient findOne(String id) {
    return jdbc.queryForObject(
        "select id, name, type from Ingredient where id=?",
        this::mapRowToIngredient,
        id
    );
        }

private Ingredient mapRowToIngredient(ResultSet rs, int rowNum)
    throws SQLException {
        return new Ingredient(
            rs.getString("id"),
            rs.getString("name"),
            Ingredient.Type.valueOf(rs.getString("type"))
        );
    }
```

### Repository

```java
package tacos.data;
import tacos.Ingredient;

public interface IngredientRepository {
    Iterable<Ingredient> findAll();
    Ingredient findOne(String id);
    Ingredient save(Ingredient ingredient);
}
```

```java
package tacos.data;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;
import tacos.Ingredient;

@Repository
public class JdbcIngredientRepository implements IngredientRepository {
    private JdbcTemplate jdbc;

    @Autowired
    public JdbcIngredientRepository(JdbcTemplate jdbc) {
        // jdbc injected by DI
        this.jdbc = jdbc;
    }

    @Override
    public Iterable<Ingredient> findAll() {
        return jdbc.query(
            "select id, name, type from Ingredient",this::mapRowToIngredient
        );
    }
    @Override
    public Ingredient findOne(String id) {
        return jdbc.queryForObject(
            "select id, name, type from Ingredient where id=?",
            this::mapRowToIngredient,
            id
        );
    }

    private Ingredient mapRowToIngredient(ResultSet rs, int rowNum)
        throws SQLException {
            return new Ingredient(
            rs.getString("id"),
            rs.getString("name"),
            Ingredient.Type.valueOf(rs.getString("type"))
        );
    }

    @Override
    public Ingredient save(Ingredient ingredient) {
        jdbc.update(
            "insert into Ingredient (id, name, type) values (?, ?, ?)",
            ingredient.getId(),
            ingredient.getName(),
            ingredient.getType().toString()
        );
        return ingredient;
    }
}
```

### Database Schemas

If there is a file named schema.sql in the root of the application's classpath, the SQL in the file will be executed against the database when the application starts.

```sql
create table if not exists Ingredient (
    id varchar(4) not null,
    name varchar(25) not null,
    type varchar(10) not null
);
create table if not exists Taco (
    id identity,
    name varchar(50) not null,
    createdAt timestamp not null
);
create table if not exists Taco_Ingredients (
    taco bigint not null,
    ingredient varchar(4) not null
);
```

## Interfaces

### KeyHolder

Interface for retrieving keys, typicall used for auto-generated keys as potentially returned by JDBC insert statements. Keys are returned as a List containing one Map for each row of keys i.e. keys are held in a List of Maps.

Most applications only use one key per row and process only one row at a time in an insert statement.

### PreparedStatementCreator

Creates a Prepared statement given a conenction, provided by the JdbcTemplate class.

```java
private long saveTacoInfo(Taco taco) {
    taco.setCreatedAt(new Date());
    PreparedStatementCreator psc = new PreparedStatementCreatorFactory(
        "insert into Taco (name, createdAt) values (?, ?)",
        Types.VARCHAR, Types.TIMESTAMP
    ).newPreparedStatementCreator(
        Arrays.asList(
            taco.getName(),
            new Timestamp(taco.getCreatedAt().getTime())
        )
    );
    KeyHolder keyHolder = new GeneratedKeyHolder();
    jdbc.update(psc, keyHolder);
    return keyHolder.getKey().longValue();
 }
```
