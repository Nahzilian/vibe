import axios from 'axios';

import { GET_USERS } from './types';

//GET USERS

export const getUsers = () => dispatch => {
    axios.get('/api/leads/')
    .then(res => {
        dispatch({
            type:GET_USERS,
            payload:res.data
        })
    }).catch(err => console.log(err));
}