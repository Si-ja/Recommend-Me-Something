<template>
<div id="app">
    <div class="topnavEssential">
      <a class="active" href="home">Home</a>
      <a href="units">Entries</a>
      <a href="management">Database</a>
      <a href="about">About</a>
    </div> 


    <div id="appEssential">
      <img src="./assets/TempBanner.png"> 
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body {
  background-color: #ffcc66;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
/* Add a black background color to the top navigation */
.topnavEssential {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #ffcc66;
  overflow: hidden;
  margin-bottom: 10px;
}
/* Style the links inside the navigation bar */
.topnavEssential a {
  float: center;
  color: #2c3e50;
  text-align: center;
  padding: 30px 30px;
  text-decoration: none;
  font-size: 20px;
}
/* Change the color of links on hover */
.topnavEssential a:hover {
  color: black;
  text-decoration: underline;
}
</style>
