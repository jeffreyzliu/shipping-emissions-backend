import React from 'react';
import {Input} from 'semantic-ui-react';
import './App.css'
import TableExamplePagination from "./table";

class App extends React.Component {
    constructor(props, context) {
        super(props, context)
    }

    showTable() {
        let dict = {'id': ["hi", "yo"]}
        return TableExamplePagination(dict)
    }


    render() {

        return (
            <div>
                <div className="ui loading icon input"><input type="text" placeholder="Search..."/><i aria-hidden="true"
                                                                                                      className="user icon"></i>
                    <div>{this.showTable()}</div>
                </div>
            </div>
        );
    }
}

export default App;