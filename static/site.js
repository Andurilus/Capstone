const vm = new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data: {
        apod: {},
        arand: {},
        mars: {},
        userData: {},
        userFilter: "",
        showRand: true,
        currentUser: {},
        apiData: "",
        newTitle: "",
        newExplanation: "",
        showData: "",
        csrf_token: "",
    },

    methods: {
        loadAPOD: function() {
            axios({
                method: 'get',
                url: 'https://api.nasa.gov/planetary/apod',
                params: {
                    
                    api_key: os.environ.get('apikey'),
                    date: this.userFilter
                    
                }
            }).then((response) => {
                this.apod = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        loadMars: function() {
            axios({
                method: 'get',
                url: 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos',
                params: {
                    api_key: os.environ.get('apikey'),
                    earth_date: this.userFilter
                }
            }).then((response) => {
                this.mars = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        loadRand: function() {
            axios({
                method: 'get',
                url: 'https://api.nasa.gov/planetary/apod',
                params: {
                    
                    api_key: os.environ.get('apikey'),
                    count: 3
                
                }
            }).then((response) => {
                this.arand = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        createApod: function(info) {
            let today = new Date()
            let yyyy = today.getFullYear()
            let mm = today.getMonth() + 1
            let dd = today.getDate()

            if (dd < 10) dd = '0' + dd
            if (mm < 10) mm = '0' + mm

            let date = yyyy + '-' + mm + '-' + dd
            
            
            axios({
                
                method: 'post',
                url: '/apis/apod/',
                headers: {
                    "X-CSRFToken": this.csrf_token
                },
                data: {
                    "author": this.currentUser.id,
                    "date": date,
                    "title": info.title,
                    "url": info.url,
                    "explanation": info.explanation,
                    "media": info.media_type
                }
            })
        },
        createMars: function(info) {
            let today = new Date()
            let yyyy = today.getFullYear()
            let mm = today.getMonth() + 1
            let dd = today.getDate()

            if (dd < 10) dd = '0' + dd
            if (mm < 10) mm = '0' + mm

            let date = yyyy + '-' + mm + '-' + dd
            
            
            axios({
                
                method: 'post',
                url: '/apis/mars/',
                headers: {
                    "X-CSRFToken": this.csrf_token
                },
                data: {
                    "author": this.currentUser.id,
                    "date": date,
                    "sol": info.sol,
                    "earth_date": info.earth_date,
                    "rover": info.rover.name,
                    "camera_name": info.camera.name,
                    "url": info.img_src,
                    
                }
            })
        },
        loadCurrentUser: function() {
            axios({
                method: 'get',
                url: '/apis/currentuser/'
            }).then(response => this.currentUser = response.data)
        },
        loadUserData: function() {
            
            axios({
                method: 'get',
                url: this.apiData,
                params: {
                    "author": this.currentUser.id
                }
            }).then(response => this.userData = response.data)
        },
        editUserData: function(info) {
            axios({
                method: 'patch',
                url: `${this.apiData}${info.id}`,
                headers: {
                    "X-CSRFToken": this.csrf_token
                },
                data: {
                    "title": info.title,
                    "explanation": info.explanation
                }
            })
        },
        deleteUserData: function(info) {
            axios({
                method: 'delete',
                url: `${this.apiData}${info.id}`,
                headers: {
                    "X-CSRFToken": this.csrf_token
                }
            })
        }
    },
    created: function() {
        this.loadRand()
        this.loadCurrentUser()
    },
    mounted: function() {
        this.csrf_token = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})