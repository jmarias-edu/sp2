import axios from 'axios'
import Cookies from 'js-cookie'


export default axios.create({
	baseURL: process.env.VUE_APP_API_URL,
	timeout: 50000,
	headers: {
		"X-CSRFToken": Cookies.get('csrftoken'),
		"Content-Type": "application/x-www-form-urlencoded",
		"Authorization": Cookies.get('authtoken'),
	}
})