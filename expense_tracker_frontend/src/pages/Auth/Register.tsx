import axios from "axios";
import {FormEvent, useState} from "react";
import {useNavigate} from "react-router-dom";
import {NavbarEmpty} from "../../components/NavbarEmpty";
import {observer} from "mobx-react-lite";
import {useToken} from "../../utils/AuthContext";
import {getApiUrlForCurrentWindow} from "../../utils/Network";
import {Col, Form, Row, Container} from "react-bootstrap";
import {SubmitButton} from "../../components/SubmitButton";

export const Register = () => {
  const auth = useToken();

  let bodyParameters = {
    username: "",
    email: "",
    password: "",
  };
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  if (auth.getToken() !== "") {
    navigate("/transactions");
  }
  const submitHandler = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    bodyParameters.username = username;
    bodyParameters.email = email;
    bodyParameters.password = password;

    axios.post(`${getApiUrlForCurrentWindow()}register`, bodyParameters).then((res)=>{
      navigate("/login");
    })
  };
  return (
    <Container>
      <NavbarEmpty />
      <Form id="login-form" onSubmit={submitHandler}>
        <Form.Group>
          <Row className="mb-3">
            <Col xs={4} sm={2} className="text-end">
              <Form.Label htmlFor="id_username">Username</Form.Label>
            </Col>
            <Col xs={8} sm={10}>
              <Form.Control
                type="text"
                name="username"
                key="id_username"
                required={true}
                onChange={(e) => setUsername(e.target.value)}
              />
            </Col>
          </Row>
          <Row className="mb-3">
            <Col xs={4} sm={2} className="text-end">
              <Form.Label htmlFor="id_email">Email</Form.Label>
            </Col>
            <Col xs={8} sm={10}>
              <Form.Control
                type="text"
                name="email"
                key="id_email"
                required={true}
                onChange={(e) => setEmail(e.target.value)}
              />
            </Col>
          </Row>
          <Row className="mb-3">
            <Col xs={4} sm={2} className="text-end">
              <Form.Label htmlFor="id_password">Password</Form.Label>
            </Col>
            <Col xs={8} sm={10}>
              <Form.Control
                type="password"
                name="password"
                key="id_password"
                required={true}
                onChange={(e) => setPassword(e.target.value)}
              />
            </Col>
          </Row>
          <SubmitButton text="Register" />
        </Form.Group>
      </Form>
    </Container>
  );
};
