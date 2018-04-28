//getting information from the database
import React, { Component } from 'react';
import Form1 from '../Components/Form1.js';

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
      return(
          <div>
            <h1>hi</h1>
            <Form1/>


            </div>


      )
  }

}

export default Home
