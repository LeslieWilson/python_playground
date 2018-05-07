//getting information from the database
import React, { Component } from 'react';
import Form1 from '../Components/Form1.js';
import Result from '../Components/Result.js';

// class Home takes the
class Home extends Component{
    constructor(props){
        super(props)
        this.state= {
            results: [],
        }
    }

componentDidMount() {
    fetch('http://localhost:5000/api/Home', {
      credentials: 'same-origin',
      method: 'GET',
      headers: { 'Content-Type':'application/json'}
    })
      .then(response => {
        if (response.ok) {
          return response;
        } else {
          let errorMessage = `${response.status} (${response.statusText})`,
          error = new Error(errorMessage);
          throw(error);
        }
      })
      .then(response => response.json())
      .then(body => {console.log(body)
        this.setState({results: body})
      })
      .catch(error => console.error(`Error in fetch: ${error.message}`));
  }

  render(){
      let results = this.state.results.map((result, index) => {
          return(
              <Result key={index}
              city = {result.city}
              state = {result.state}
              country = {result.country}
              email = {result.email}
              name = {result.name}
              zip = {result.zip}
              />

          )
      })

    //   const todoItems = todos.map((todo, index) =>
    //     // Only do this if items have no stable IDs
    //     <li key={index}>
    //       {todo.text}
    //     </li>
    //   );

      return(
          <div>
            <h1>hi</h1>
            <Form1/>
            {results}
            </div>


      )
  }

}

export default Home
