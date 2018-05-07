import React, { Component } from 'react';

class Form1 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        name: '',
        email: '',
        country: '',
        state: '',
        city: '',
        street: '',
        zip: ''

    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
      const target = event.target;
      const value = target.value
      const name = target.name;

    this.setState({
    [name]: value
    });

}
//send information to the databse

  handleSubmit(event) {
    event.preventDefault();
    fetch('http://localhost:5000/api/Home', {
      credentials: 'same-origin',
      method: 'POST',
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
    return (
      <form onSubmit={this.handleSubmit}>

        <label>
          Name:
          <input type="text" name= "name" value={this.state.name} onChange={this.handleChange} />
        </label>
        <label>
          Email:
          <input type="text" name= "email" value={this.state.email} onChange={this.handleChange} />
        </label>
        <label>
          Country:
          <input type="text" name= "country" value={this.state.country} onChange={this.handleChange} />
        </label>
        <label>
          State:
          <input type="text" name = "state" value={this.state.state} onChange={this.handleChange} />
        </label>
        <label>
          City:
          <input type="text" name = "city" value={this.state.city} onChange={this.handleChange} />
        </label>
        <label>
          Street:
          <input type="number" name = "street" value={this.state.street} onChange={this.handleChange} />
        </label>
        <label>
          Zip:
          <input type="number" name= "zip" value={this.state.zip} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />

      </form>
    );
  }
}

export default Form1
