import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import LeClient from 'legimens'

export wrapModuleWithLegimens = (Pres) => ({data, addr}) =>
  console.debug 'wrapping pres', Pres.constructor.name
  L.div className:'contents',
    L_ LeClient, addr:addr, refval:data,
      (variable, setattr) =>
        console.debug "received updates #{JSON.stringify variable}"
        if variable is undefined
          variable = value:'Loading', type:'raw'
          return "Loading"
        else
          try
            variable = JSON.parse variable
          catch
        console.debug("Returning to presenter", variable)
        L_ Pres, data:variable, addr:addr, setattr:setattr

