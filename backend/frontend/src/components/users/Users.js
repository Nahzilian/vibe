import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getUsers } from '../../actions/users';
export class Users extends Component {
    static propTypes = {
        users: PropTypes.array.isRequired
    }

    render() {
        return (
            <div>
                <h1>All users</h1>
            </div>
        )
    }
}
const mapStateToProps = state => ({
    users: state.users.users
});

export default connect(mapStateToProps)(Users);
