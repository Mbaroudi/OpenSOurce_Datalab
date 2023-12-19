cube(`MyCube`, {
  sql: `SELECT * FROM my_table`, // SQL query to fetch data from "my_table"

  measures: {
    count: {
      type: `count`,
      sql: `id`
    },
    totalQuantity: {
      type: `sum`,
      sql: `quantity`
    },
    averagePrice: {
      type: `avg`,
      sql: `price`
    }
  },

  dimensions: {
    id: {
      sql: `id`,
      type: `number`,
      primaryKey: true
    },
    name: {
      sql: `name`,
      type: `string`
    }
  }
});

