class Form(object):
    def __init__(self):
        self.page_open = '''
<!DOCTYPE html>
<html>
<head>
    <title>Lab 2: Simple Form</title>
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.4.2/pure-min.css">
    <link href="css/style.css" rel="stylesheet" type="text/css">
</head>
<body>
    <div class="pure-g">
        <div class="pure-u-1-3" id="wrapper">
        '''
        self.page_result = '''
            <h1>Thank you for signing in to DPWP!</h1>

        '''
        self.page_content = '''
            <h1>Welcome to DPWP!</h1>
            <h3>Please sign in to continue...</h3>
            <form method="GET" action="" class="pure-form" id="form">
                <fieldset class="pure-group">
                    <input type="text" class="pure-input-1" name="username" placeholder="Username">
                    <input type="password" class="pure-input-1" name="password" placeholder="Password">
                    <input type="password" class="pure-input-1" name="password2" placeholder="Confirm Password">
                    <input type="email" class="pure-input-1" name="email" placeholder="Email">
                </fieldset>

                <fieldset class="pure-group">
                    <input type="text" class="pure-input-1" name="firstname" placeholder="First Name">
                    <input type="text" class="pure-input-1" name="lastname" placeholder="Last Name">
                </fieldset>
                <div class="pure-control-group" id="radio-btn">
                    <input type="radio" name="sex" value="Male" id="male"> Male
                    <input type="radio" name="sex" value="Female" id="female"> Female
                </div>
                <fieldset class="pure-group">
                    <input type="text" class="pure-input-1" name="address" placeholder="Address">
                    <input type="text" class="pure-input-1" name="city" placeholder="City">
                    <select id="state" name="state">
                        <option value="" selected="selected">Select a State</option>
                        <option value="AL">Alabama</option>
                        <option value="AK">Alaska</option>
                        <option value="AZ">Arizona</option>
                        <option value="AR">Arkansas</option>
                        <option value="CA">California</option>
                        <option value="CO">Colorado</option>
                        <option value="CT">Connecticut</option>
                        <option value="DE">Delaware</option>
                        <option value="DC">District Of Columbia</option>
                        <option value="FL">Florida</option>
                        <option value="GA">Georgia</option>
                        <option value="HI">Hawaii</option>
                        <option value="ID">Idaho</option>
                        <option value="IL">Illinois</option>
                        <option value="IN">Indiana</option>
                        <option value="IA">Iowa</option>
                        <option value="KS">Kansas</option>
                        <option value="KY">Kentucky</option>
                        <option value="LA">Louisiana</option>
                        <option value="ME">Maine</option>
                        <option value="MD">Maryland</option>
                        <option value="MA">Massachusetts</option>
                        <option value="MI">Michigan</option>
                        <option value="MN">Minnesota</option>
                        <option value="MS">Mississippi</option>
                        <option value="MO">Missouri</option>
                        <option value="MT">Montana</option>
                        <option value="NE">Nebraska</option>
                        <option value="NV">Nevada</option>
                        <option value="NH">New Hampshire</option>
                        <option value="NJ">New Jersey</option>
                        <option value="NM">New Mexico</option>
                        <option value="NY">New York</option>
                        <option value="NC">North Carolina</option>
                        <option value="ND">North Dakota</option>
                        <option value="OH">Ohio</option>
                        <option value="OK">Oklahoma</option>
                        <option value="OR">Oregon</option>
                        <option value="PA">Pennsylvania</option>
                        <option value="RI">Rhode Island</option>
                        <option value="SC">South Carolina</option>
                        <option value="SD">South Dakota</option>
                        <option value="TN">Tennessee</option>
                        <option value="TX">Texas</option>
                        <option value="UT">Utah</option>
                        <option value="VT">Vermont</option>
                        <option value="VA">Virginia</option>
                        <option value="WA">Washington</option>
                        <option value="WV">West Virginia</option>
                        <option value="WI">Wisconsin</option>
                        <option value="WY">Wyoming</option>
                    </select>
                    <select id="country" name="country">
                        <option value="USA">United States</option>
                        <option value="Can">Canada</option>
                        <option value="UK">United Kingdom</option>
                    </select>
                    <input type="text" class="pure-input-1" name="zip" placeholder="Zip/Postal Code">
                </fieldset>
                <label for="terms" class="pure-checkbox" id="checkbox">
                <input type="checkbox" name="terms" value="true" id="terms"> Accept Terms & Conditions
                </label>
                <button type="submit" name="submit" class="pure-button pure-input-1 pure-button-primary">Sign In</button>
            </form>
        '''
        self.page_close = '''
        </div>
    </div>


</body>
</html>
        '''

    def print_content(self, content=""):

        return self.page_open + self.page_content + content + self.page_close

    def print_result(self, result=""):

        return self.page_open + self.page_result + result + self.page_close


