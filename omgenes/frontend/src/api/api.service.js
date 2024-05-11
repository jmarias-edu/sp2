import axios from 'axios'
import Cookies from 'js-cookie'

export default axios.create({
	baseURL: "http://localhost:8000/",
	timeout: 5000,
	headers: {
		'Access-Control-Allow-Origin': '*',
		"Content-Type": "application/x-www-form-urlencoded",
		'X-CSRFToken': Cookies.get('csrftoken'),
	}
})