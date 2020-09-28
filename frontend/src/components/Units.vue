<template>
    <div id="optionsDiv">
        <div id="optionsSelection">
            <p>Chose a Type</p>
            <select v-model="table_selected" @change="loadDatabaseInformation()">
                <option disabled value="">Available Databases</option>
                <option v-for="table in tables" v-bind:key="table">
                    {{ table }}
                </option>
            </select>
        </div>

        <div id="allOfEntries">
            <select v-model="content_selected" @change="loadSingleEntry()">
                <option disabled value="">Existing Entries</option>
                <option v-for="content in contents" v-bind:key=content>
                    {{ content }}
                </option>
            </select>
        </div>

        <div id="formInformation">
            <input v-model="prod_name" placeholder="Product's Name">
            <br>
            <input v-model="prod_year" placeholder="Product's Year">
            <br>
            <input v-model="prod_img" placeholder="Product's Image Source">
            <br>
            <textarea style="width: 230px; height: 160px;" v-model="prod_description" placeholder="Product's Description"></textarea>
            <br>
            <button @click="clickNewUpdate()">Edit/New</button>
        </div>
    </div>
</template>

<style scoped>
#allOfEntries {
    padding: 2rem;
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
            content_selected: '',
            prod_name: '',
            prod_year: '',
            prod_description: '',
            prod_img: '',
        }
    },
    methods: {
        updateInputToEmpty() {
            // Clear the input boxes
            this.prod_name = '',
            this.prod_year = '',
            this.prod_img = '',
            this.prod_description = ''
        },
        loadSingleEntry() {
            //Load an object of information for a single selected entry
            const path = `http://localhost:5000/api/` + this.table_selected + `/` + this.content_selected
            axios.get(path)
                .then(response => {
                    this.prod_name = response.data.name,
                    this.prod_year = response.data.year,
                    this.prod_img = response.data.img,
                    this.prod_description = response.data.description
                })
                .catch(error => {
                    console.log("Could not retrieve a single items information")
                })
        },
        clickNewUpdate() {
            //This method checks whether a new entry should be made, or an old one updated
            // Update happens if an entry is selected beforehand. And a new one, if it is not.
            if (this.prod_name != this.content_selected) {
                const payload = this.payloadGenerator();
                const path = `http://localhost:5000/api/` + this.table_selected + `/` + this.prod_name + `/add`
                axios.post(path, payload)
                    .then(response => (window.alert("Item: " + this.prod_name + " has been added.")))
                    .then(response => (updateInputToEmpty()))
                    .then(respone => (loadDatabaseInformation()))
                .catch((error) => {
                    console.log("Couldn't add " + this.prod_name)
                })
            }
            else {
                const payload = this.payloadGenerator();
                const path = `http://localhost:5000/api/` + this.table_selected + `/` + this.prod_name + `/edit`
                axios.put(path, payload)
                    .then(response => (window.alert("Item: " + this.prod_name + " has been updated.")))
                    .then(response => (updateInputToEmpty()))
                .catch((error) => {
                    console.log("Couldn't update " + this.prod_name)
                })
            }
        },
        payloadGenerator() {
            // A method that helps create a payload that will be sent to an api request
            const payload = {
                prod_name: this.prod_name,
                prod_year: this.prod_year,
                prod_img: this.prod_img,
                prod_description: this.prod_description
            }
            return payload
        },
        loadDatabaseInformation() {
            //Get all contents of a particular table in the database
            //The table itself is chosen independently and is stored in the table_selected obj
            const path = `http://localhost:5000/api/` + this.table_selected + `/contents`
            axios
                .get(path)
                .then(response => (this.contents = response.data))
                .then(response => (this.updateInputToEmpty()))
                .finally(response => (this.content_selected = ''))
            .catch(error => {
                    console.log("Couldn't retrieve tables")
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