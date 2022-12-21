// import React from 'react'
import React,{useState , useEffect} from 'react'
import { Link} from 'react-router-dom'
import {Form , Button , Row , Col } from 'react-bootstrap'
import Loader from '../Loader'
import Message from '../Message'
import { useSelector, useDispatch } from 'react-redux'
import { register } from '../actions/userActions'
import FormContainer from '../FormContainer'
import {BrowserRouter as Router, Switch, Route} from  'react-router-dom'
// import { useHistory } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';



function RegisterScreen({Location}) {
        const [name, setName] = useState('')
        const [password, setPassword] = useState('')
        const [email, setEmail] = useState('')
        const [ConfirmPassword, setConfirmPassword] = useState('')
        const [message, setMessage] = useState('')
        
        const dispatch = useDispatch()
        // const history = useHistory();
        const history = useNavigate()
        const redirect = window.location.search ? window.location.search.split('=')[1] : '/'
    
        const userRegister = useSelector(state => state.userRegister)
        const {error,loading,userInfo} = userRegister
    
        useEffect(() =>{
            if (userInfo)
            {
                history(redirect)
            }},[history , userInfo , redirect]
        )
    
    
        const submitHandler = (e) =>
        {
            e.preventDefault()
            if (password != ConfirmPassword)
            {
                setMessage('Passswords do not mach')
            }
            else {
                dispatch(register(name , email , password))
            }
            

        }

  return (
    <FormContainer>
    <h1>Sign In</h1>
    {message && <Message variant = 'danger'>{message}</Message>}
    {error && <Message variant = 'danger'>{error}</Message>}
    {loading && <Loader/>}
      <Form onSubmit = {submitHandler}>

      <Form.Group controlId = 'name'>
            <Form.Label>Name</Form.Label>
            <Form.Control
                required
                type = 'name'
                placeholder = 'Enter name'
                value = {name}
                onChange = {(e) => setName(e.target.value)}
            ></Form.Control>
            
        </Form.Group>

        <Form.Group controlId = 'email'>
            <Form.Label>Email Address</Form.Label>
            <Form.Control
                required
                type = 'email'
                placeholder = 'Enter Email'
                value = {email}
                onChange = {(e) => setEmail(e.target.value)}
            ></Form.Control>
            
        </Form.Group>

        <Form.Group controlId = 'password'>
            <Form.Label>Password</Form.Label>
            <Form.Control
                required
                type = 'password'
                placeholder = 'Enter Password'
                value = {password}
                onChange = {(e) => setPassword(e.target.value)}
            ></Form.Control>
        </Form.Group>

        <Form.Group controlId = 'passwordConfirm'>
            <Form.Label>Confirm Password</Form.Label>
            <Form.Control
                required
                type = 'password'
                placeholder = 'Conirm Password'
                value = {ConfirmPassword}
                onChange = {(e) => setConfirmPassword(e.target.value)}
            ></Form.Control>
        </Form.Group>

        <Button type = 'submit' variant = 'primary' >
            Register</Button>
    
            </Form>
            <Row className='py-3'>
        <Col>
        Have an Account?
        <Link to={redirect ? `/login?redirect=${redirect}` : '/login'}>
        Sign In
        </Link>
        </Col>
    </Row>


    </FormContainer>
  )
}

export default RegisterScreen
