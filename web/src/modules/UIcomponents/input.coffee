import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

export default class Input extends React.Component
  constructor:(props)->
    super(props)
    @state = {}
    @state.value=props.default
    @value = props.default

  onChange:(event)=>
    console.log event, event.target.value
    value = event.target.value
    @setState value:value
    @value = value
    @props.onChange event.value

  get_style:(value)->
    borderRadius:3
    width:value?.length*7+10
    border:1
    padding:4

  render:() ->
    {value} = @state
    L.input
      type:'text'
      style:@get_style value
      value:value
      onChange:@onChange
