path = require 'path'
webpack = require 'webpack'

HtmlWebpackPlugin = require 'html-webpack-plugin'
ExtractTextPlugin = require 'extract-text-webpack-plugin'

isProduction = process.env.NODE_ENV is 'production'

cssDev = ['style-loader', 'css-loader']
cssProd = ExtractTextPlugin.extract
  fallback: 'style-loader'
  use: ['css-loader']
  publicPath: '/dist'

cssConfig = if isProduction then cssProd else cssDev

module.exports =
  entry: 
    installed: ['./BirModule']
  output:
    filename: 'installed.js'
    #path: path.resolve(__dirname, '../../../../dist')
    path: path.resolve(__dirname, 'dist')
    library: 'installed_[hash]'
  module:
    rules: [
      {
        test: /\.coffee$/,
        use: [
          {
            loader: 'babel-loader'
            options:
              presets: ['@babel/preset-env', '@babel/preset-react'],
          }
          'coffee-loader'
        ],
        exclude: /node_modules/
      },
      {
        test: /\.less$/,
        use: [{
          loader: 'style-loader' ,
        }, {
          loader: 'css-loader',
        }, {
          loader: 'less-loader',
        }],
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },

    ]
  plugins: [
    new ExtractTextPlugin
      filename: 'app.css'
      disable: !isProduction
      allChunks: true
    new webpack.NamedModulesPlugin()
    new webpack.DllPlugin
      name: 'installed_[hash]'
      path: path.resolve(__dirname, 'dist/installed-manifest.json')

  ]
