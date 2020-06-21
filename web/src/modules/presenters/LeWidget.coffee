import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import LeClient from 'legimens'

export wrapModuleWithLegimens = (Pres) => ({data, addr}) =>
  console.log 'Vis object with ref #{data} uses', Pres
  L.div className:'contents',
    L_ LeClient, addr:addr, refval:data,
      (variable, setattr) =>
        console.log "in wrapper of #{Pres} variable #{variable} ref #{data}"
        if variable is undefined
          variable = value:'Loading', type:'raw'
          return "Loading"
        else
          try
            variable = JSON.parse variable
          catch
        console.debug "Displaying object",data, variable
        L_ Pres, data:variable, addr:addr, setattr:setattr

