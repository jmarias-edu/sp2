import axios from 'axios'
import Cookies from 'js-cookie'


export default axios.create({
	baseURL: "http://localhost:8080/",
	timeout: 10000,
	headers: {
		"X-CSRFToken": Cookies.get('csrftoken'),
		"Content-Type": "application/x-www-form-urlencoded",
		"Authorization": Cookies.get('authtoken'),
	}
})