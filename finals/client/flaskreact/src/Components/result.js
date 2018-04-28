// import ReactDOM from 'react-dom';
// import React, {Component} from 'react';
// class Form1 extends Component{
//     render(){
//         return (
//             <div class="form">
//                 <form action="http://localhost:5000/result" method="get">
//                     databaseEntry: <input type="text" name="place"/>
//                     <input type="submit" value="Submit"/>
//                 </form>
//             </div>
//         );
//     }
// }
//
//
// export default Form1


import reactDOM from 'react-dom';
import React, {Component} from 'react';

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

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.name);
    event.preventDefault();
  }

  render() {
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
