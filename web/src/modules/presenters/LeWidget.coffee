import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import LeClient from 'legimens'
import {choosePresenter} from '../visualiser.coffee'

export wrapLeWidget = (Pres) => ({data, addr}) =>
  console.log 'wrapping pres',Pres
  L.div className:'container',
    L_ LeClient, addr:addr, refval:data,
      (variable, setattr) =>
        console.log "in wrapper of #{Pres} variable #{variable}"
        if variable is undefined
          variable = value:'Loading', type:'raw'
          return "Loading"
        else
          variable = JSON.parse variable
        L_ Pres, data:variable, addr:addr, setattr:setattr

export default LeWidget = ({data, addr})->
  L.div className:'container',
    L_ LeClient, addr:addr, refval:data,
      (variable, setattr) =>
        if variable is undefined
          variable = value:'Loading', type:'raw'
        else
          variable = JSON.parse variable
        console.log('in le_widget choosePresenter', variable)
        Pres = choosePresenter variable.type, variable
        L_ Pres, data:variable, addr:addr, setattr:setattr

