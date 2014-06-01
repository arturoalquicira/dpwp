class Page(object):
    def __init__(self):
        self.open = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Homes, Apartments & Rooms For Rent - BookIt.me</title>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <link rel="stylesheet" href="//code.jquery.com/ui/1.10.4/themes/smoothness/jquery-ui.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="//code.jquery.com/ui/1.10.4/jquery-ui.js"></script>

</head>
<body>
'''
        self.anim_bck = '''
<img id="background" alt="background" src="" />
'''
        self.nav_bar = '''
<div class="container-fluid" id="container">
    <div class="row">
        <nav class="navbar navbar-default" role="navigation">
            <div class="container-fluid">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                  <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                  </button>
                  <a class="navbar-brand" href="#">BookIt.me</a>
                </div>
            </div><!-- /.container-fluid -->
        </nav>
    </div>
'''

        self.filters = '''
    <div class="row" id="main-container">
        <div class="col-md-12">
            <div class="row">
                <!-- Filters Sidebar -->
                <div class="col-md-4" id="filters" data-spy="affix">
                    <form class="" role="form">
                        <div class="form-group">
                            <label class="sr-only" for="place">Email address</label>
                            <input autofocus type="text" class="form-control input-lg" id="place" name="place" placeholder="Look for a place...">
                        </div>
                        <div class="form-group ">
                            <label class="sr-only" for="from2">Password</label>
                            <input type="text" class="form-control input-lg" id="from2" name="checkin" placeholder="Check-In">
                        </div>
                        <div class="form-group">
                            <label class="sr-only" for="to2">Password</label>
                            <input type="text" class="form-control input-lg" id="to2" name="checkout" placeholder="Check-Out">
                        </div>
                        <button id="btn-search" type="submit" name="submit" class="btn btn-primary btn-lg btn-block">Search <span class="glyphicon glyphicon-search"></span></button>
                    </form>
                </div> <!-- Ends Filters Sidebar -->
                <!-- Main Content / Listing results -->
                <div class="col-md-8 col-md-offset-4">


'''
        self.content = '''

'''
        self.close = '''
            </div>
        </div>
    </div>
</div>

<script src="js/main.js"></script>
<script src="js/rainyday.js"></script>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
</body>
</html>

'''
        self.all = ""

    # def print_out(self):
    #     self.update()
    #     return self.all
    #
    # def update(self):
    #     self.all = self.open + self.nav_bar + self.content + self.close
    #     self.all = self.all.format(**locals())


class FormPage(Page):
    def __init__(self):
        # call the constructor function of the parent
        Page.__init__(self)
        self.form_open = '''
    <div class="row" id="header">
        <div class="col-md-6 col-md-offset-1">
            <h1>Traveling?</h1>
            <h2>Find a place to stay...</h2>
        </div>
    </div>
    <div class="row">
        <div class="col-md-9 col-md-offset-1" id="home-form">

            <form class="form-inline" role="form" method="GET">


        '''
        self.inputs = """
                <div class="form-group ">
                    <label class="sr-only" for="place">Enter a Place</label>
                    <input autofocus type="text" class="form-control input-lg" id="place" name="place" placeholder="Look for a place...">
                </div>
                <div class="form-group ">
                    <label class="sr-only" for="from">Check-In</label>
                    <input type="text" class="form-control input-lg" id="from" name="checkin" placeholder="Check-In">
                </div>
                <div class="form-group">
                    <label class="sr-only" for="to">Check-Out</label>
                    <input type="text" class="form-control input-lg" id="to" name="checkout" placeholder="Check-Out">
                </div>
                <button id="btn-search" type="submit" name="submit" class="btn btn-primary btn-lg">Search <span class="glyphicon glyphicon-search"></span></button>
        """
        self.form_close = '''
            </form>
        </div>
    </div>

        '''

    def page_home(self):
        self.all = self.open + self.anim_bck + self.nav_bar + self.form_open + self.inputs + self.form_close + self.close
        self.all = self.all.format(**locals())
        return self.all