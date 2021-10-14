import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ServerStore from "../stores/ServerStore.jsx"
import Cookies from 'js-cookie';


const CSRFToken = () => {
    const [csrftoken, setcsrftoken] = useState('');

    const getCookie = (name) => {
        console.log(name)
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            console.log(cookies)
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    console.log(cookieValue)
                    Cookies.set('csrftoken', cookieValue)
                    
                    break;
                }
            }
        }
        return cookieValue;
    }

    useEffect(() => {
        const fetchData = async () => {
            try {
                fetch(`${ServerStore.url}/api/user/`,{
                    credentials: 'include'
                }).then(res => {
                    console.log(res)
                })
            } catch (err) {

            }
        };

        fetchData();
        setcsrftoken(getCookie('csrftoken'));
    }, []);

    return (
        <input type='hidden' name='csrfmiddlewaretoken' value={csrftoken} />
    );
};

export default CSRFToken;