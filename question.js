import React, {useState} from 'react'
import Link from 'next/link'
// import '../styles/main.scss'

export default class extends React.Component {
constructor(props){
super(props)
  this.state = { content: "" }
  this.update=this.update.bind(this)
}

update(event){
        // setContent(event.target.value);
        this.setState({content:event.target.value})
    }
    
render() {
   return (<div>
        <h1><font face="Arial" size="40px" color="#FF7A59">Welcome to OpenCell.</font></h1>
         <font face="Arial" size="10px"> </font>
        <textarea value={this.state.content} onChange={this.update}></textarea>
        {this.state.content}
        <ul>
            <li><Link href='/add'><a><font face="Arial" size="10px">Contact an incarcerated person.</font></a></Link></li>
        </ul>
    </div>);
 }
}