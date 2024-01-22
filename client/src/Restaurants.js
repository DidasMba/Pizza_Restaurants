// App.js

import React, { useState, useEffect } from 'react';

function Restaurant() {
  const [restaurants, setRestaurants] = useState([]);
  const [pizzas, setPizzas] = useState([]);
  const [newPizza, setNewPizza] = useState({
    price: '',
    pizza_id: '',
    restaurant_id: '',
  });

  useEffect(() => {
    // Chargement initial des restaurants et pizzas
    fetchRestaurants();
    fetchPizzas();
  }, []);

  const fetchRestaurants = async () => {
    try {
      const response = await fetch('/restaurants');
      const data = await response.json();
      setRestaurants(data);
    } catch (error) {
      console.error('Error fetching restaurants:', error);
    }
  };

  const fetchPizzas = async () => {
    try {
      const response = await fetch('/pizzas');
      const data = await response.json();
      setPizzas(data);
    } catch (error) {
      console.error('Error fetching pizzas:', error);
    }
  };

  const handleDeleteRestaurant = async (id) => {
    try {
      const response = await fetch(`/restaurants/${id}`, {
        method: 'DELETE',
      });

      if (response.status === 204) {
        // Mise à jour de la liste des restaurants après la suppression
        fetchRestaurants();
      } else {
        const errorData = await response.json();
        console.error('Error deleting restaurant:', errorData);
      }
    } catch (error) {
      console.error('Error deleting restaurant:', error);
    }
  };

  const handleCreateRestaurantPizza = async () => {
    try {
      const response = await fetch('/restaurant_pizzas', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newPizza),
      });

      if (response.status === 201) {
        // Mise à jour de la liste des pizzas après la création
        fetchPizzas();
      } else {
        const errorData = await response.json();
        console.error('Error creating restaurant pizza:', errorData);
      }
    } catch (error) {
      console.error('Error creating restaurant pizza:', error);
    }
  };

  return (
    <div className="App">
      <h1>React Pizza App</h1>

      <h2>Restaurants:</h2>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            {restaurant.name} - {restaurant.address}
            <button onClick={() => handleDeleteRestaurant(restaurant.id)}>
              Supprimer
            </button>
          </li>
        ))}
      </ul>

      <h2>Pizzas:</h2>
      <ul>
        {pizzas.map((pizza) => (
          <li key={pizza.id}>
            {pizza.name} - {pizza.ingredients}
          </li>
        ))}
      </ul>

      <h2>Créer une nouvelle Pizza pour un Restaurant:</h2>
      <div>
        <label>
          Prix:
          <input
            type="number"
            value={newPizza.price}
            onChange={(e) => setNewPizza({ ...newPizza, price: e.target.value })}
          />
        </label>
        <label>
          ID de la Pizza:
          <input
            type="number"
            value={newPizza.pizza_id}
            onChange={(e) => setNewPizza({ ...newPizza, pizza_id: e.target.value })}
          />
        </label>
        <label>
          ID du Restaurant:
          <input
            type="number"
            value={newPizza.restaurant_id}
            onChange={(e) => setNewPizza({ ...newPizza, restaurant_id: e.target.value })}
          />
        </label>
        <button onClick={handleCreateRestaurantPizza}>Créer Pizza</button>
      </div>
    </div>
  );
}




export default Restaurant;
