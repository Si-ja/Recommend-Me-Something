<template>
    <div>
        <div id="optionsSelection">
            <select v-model="table_selected" @change="loadDatabaseInformation()">
                <option disabled value="">Available Databases</option>
                <option v-for="table in tables" v-bind:key="table">
                    {{ table }}
                </option>
            </select>
            <!--<button style="margin-left:15px" @click="loadDatabaseInformation">Load the Database Information</button>-->
        </div>

        <!--To help with buttons: https://renatello.com/pass-parameter-to-method-vue-js/-->
        <div id="databaseInformation">
            <table class="informationTable">
                <thead>
                    <tr>
                        <th>Record</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="content in contents" v-bind:key=content>
                        <th scope="row">{{ content }}</th>
                        <th><button @click="removeEntry(content)">Remove</button></th>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<style>
#optionsSelection {
    text-align: center;
    padding: 10px;
}

th, td {
    padding: 5px;
}

table td { 
    overflow: hidden;
 }

table {
    margin-top: 30px;
    margin-left: auto;
    margin-right: auto;
}

.editbtn {
    color: black;
    background-color: yellow;
}

.deletebtn {
    color: black;
    background-color: tomato;
}
</style>


<script>
//axios will allow for bridging the connection between the frontend and the backend api
import axios from 'axios'
export default {
    data() {
        return {
            tables: null,
            table_selected: '',
            contents: null,
        }
    },
    methods: {
        loadDatabaseInformation() {
            //Get all contents of a particular table in the database
            //The table itself is chosen independently and is stored in the table_selected obj
            const path = `http://localhost:5000/api/` + this.table_selected + `/contents`
            axios
                .get(path)
                .then(response => (this.contents = response.data))
            .catch(error => {
                    console.log("Couldn't retrieve tables")
                })
        },
        removeEntry(itemId) {
            const path = `http://localhost:5000/api/` + this.table_selected + `/` + itemId + `/delete`
            axios.delete(path)
                .then(window.alert("Item: " + itemId + " from the table: " + this.table_selected + " has been deleted."))
                .then(response => (this.loadDatabaseInformation()))
            .catch(error => {
                console.log("Couldn't delete the " + itemId)
            }) 
        },
        updateTheTable() {
            //A method called each time an update occures in the system from the user's side
            // Get information on what tables the database works with
            const path = `http://localhost:5000/api/tables`
            axios
                .get(path)
                .then(response => (this.tables = response.data))
            .catch(error => {
                console.log("Error loading the database and finding a database.")
            })
        },
    },
    created() {
        this.updateTheTable();
    },
}
</script>