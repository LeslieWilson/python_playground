import ReactDOM from 'react-dom';
import React, {Component} from 'react';
class Form1 extends Component{
    render(){
        return (
            <div class="form">
                <form action="http://localhost:5000/result" method="get">
                    databaseEntry: <input type="text" name="place"/>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        );
    }
}


export default Form1
