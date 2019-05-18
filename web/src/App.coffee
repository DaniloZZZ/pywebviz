import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import GridLayout from 'react-grid-layout'
import Notebook from './modules/notebook.coffee'

import './styles/grid.css'

export default class App extends React.Component
  constructor:->
    super()
    @layout = [
        i:'notebook', x:0, y:0, w:2, h:7
      , i:'number', x:2, y:0, w:2, h:3
    ]
    console.log @layout
    

     
  render: ->
    L.div className:'app',
      L_ GridLayout,
        className:'grid'
        cols:6
        rowHeight:30
        width:1000
        layout: @layout
        L.div key:'notebook', L_ Notebook
        L.div key:'number', "hello"

