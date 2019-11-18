import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

export default class Input extends React.Component
  constructor:(props)->
    super(props)
    @state = {}
    @state.value=props.default

  onChange:(event)=>
    console.log event, event.target.value
    value = event.target.value
    @setState value:value
    @props.onChange value

  get_style:(value)->
    borderRadius:2
    width:value?.length*9+10
    border:1
    padding:3
    fontSize:16
    backgroundColor: '#f3f3f9'


  render:() ->
    {value} = @state
    L.input
      type:'text'
      style:@get_style value
      value:value
      onChange:@onChange
