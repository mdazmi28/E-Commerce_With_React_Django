import React from 'react';
import { Link } from "react-router-dom";

const Footer = () => {
    return (
        <>
            <div>
                <div className="section-bottom shadow-sm bg-light">
                    <div className="container py-5">
                        <div className="row">
                            <div className="col-md-4">
                                <h1 className="bodyMedium">Legals</h1>
                                <p className="my-2">
                                    <Link className="nav-link" to="/">About</Link>
                                </p>
                                <p className="my-2">
                                    <Link className="nav-link" to="/">Refund Policy</Link>
                                </p>
                                <p className="my-2">
                                    <Link className="nav-link" to="/">Terms</Link>
                                </p>
                            </div>
                            <div className="col-md-4">
                                <h1 className="bodyMedium">Information</h1>
                                <p className="my-2">
                                    <Link className="nav-link" to="/">How to buy</Link>
                                </p>
                                <p className="my-2">
                                    <Link className="nav-link" to="/">Contact</Link>
                                </p>
                                <p className="my-2">
                                    <Link className="nav-link" to="/">Complain</Link>
                                </p>
                            </div>
                            <div className="col-md-4">
                                <h1 className="bodyMedium">About</h1>
                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum</p>
                                <img className="w-75" src="https://securepay.sslcommerz.com/stores/invoice-banner/6463_ATT-95f5f94dbb181e35c56b4fe1d095b972-DIS-SCZ100-a2f04745390fd6897d09772b2cd1f581-5fdcab1063bc8.jpg" alt="Payment Methods"/>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="bg-dark py-3 text-center">
                    <p className="text-white bodySmal">All Rights Reserved</p>
                </div>
            </div>
        </>
    );
};

export default Footer;
