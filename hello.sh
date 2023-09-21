  #!/bin/bash
	      declare -a users=("User1" "User2" "User3")              
              a=2
              b=2
              c=$((a + b))
              
              echo "Bash says: Hello, World!"
              echo "$a + $b = $c"
	      for user in "${users[@]}"; do
		echo "$user"
		done

