import { Switch, Route } from "react-router-dom";
import Restaurant from "./Restaurants";
// Import any other necessary components here

function App() {
  return (
    <div>
      <main>
        <Switch>
          {/* Uncomment and add the necessary imports if you have RestaurantPizzaForm */}
          {/* <Route exact path="/restaurant_pizzas/new">
            <RestaurantPizzaForm />
          </Route> */}

          {/* Uncomment and add the necessary imports if you have a component for /restaurants/:id */}
          {/* <Route exact path="/restaurants/:id">
            <Restaurant />
          </Route> */}

          {/* Make sure you have imported the Restaurant component */}
          <Route exact path="/">
            <Restaurant />
          </Route>
        </Switch>
      </main>
    </div>
  );
}

export default App;
