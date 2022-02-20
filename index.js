import React from 'react'
import Link from 'next/link'
// import '../styles/main.scss'

export default () => (
    <div>
        <h1><font face="Arial" size="40px" color="#FF7A59">Welcome to OpenCell.</font></h1>
        <font face="Arial" size="10px"> </font>
        <ul>
            <li><Link href='/add'><a><font face="Arial" size="10px">Contact an incarcerated person.</font></a></Link></li>
            
        </ul>
    </div>
)