
<?php session_start();
$_SESSION['login'] = "" ?>
<html>
<!DOCTYPE html>
    <head>
       <meta charset="utf-8">
        <!-- importer le fichier de style -->
        <link rel="stylesheet" href="style.css" media="screen" type="text/css" />
    </head>
    <body>
    <?php
            function connexion(){ ?>
        <div id="container">
            <!-- zone de connexion -->
            
            <form action="verification.php" method="POST">
                <h1>Connexion</h1>
                
                <label><b>Nom d'utilisateur</b></label>
                <input type="text" placeholder="Entrer le nom d'utilisateur" name="username" required>

                <label><b>Mot de passe</b></label>
                <input type="password" placeholder="Entrer le mot de passe" name="pass" required>

                <input type="submit" id='submit' value='LOGIN' >
               
            </form>
        </div>

        <?php
		}
        if (!isset($_POST['username'])) {
			formulaire();
		}else {
			$login = $_POST['username'];
			$password = $_POST['pass'];

			if ($login == "arona" and $password == "1000") {
				$_SESSION['login'] = $login;
				header("Location:index.php");
			}else {
				formulaire();
			}
		}

	?>	
    </body>
</html>