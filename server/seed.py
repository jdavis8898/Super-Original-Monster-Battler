#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Battle, Monster, Move, Battle_User, Monster_Move

fake = Faker()

def create_users():
    users = []

    for _ in range(15):
        u = User(
            username=fake.first_name(),
            computer=False
        )
        u.password_hash = "ppp"
        users.append(u)
    
    for _ in range(5):
        u = User(
            username=fake.first_name(),
            computer=True
        )
        users.append(u)

    return users

# def create_battles():
#     battles = []

#     for _ in range(10):
#         b = Battle(
#             user_turn=false
#             complete=true
#         )

def create_monsters():
    monsters = []

    m1 = Monster(
        name="FireDino",
        type="Fire",
        health=20,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzkOuDkFlUlmT6189ICgM40mKiY-uvj3khNQ&usqp=CAU"
    )
    monsters.append(m1)

    m2 = Monster(
        name="WaterDevil",
        type="Water",
        health=20,
        image="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxIQEhUTEBMWFhUVGBYVGBgYFxgdHhYVGBkXFhgXGBgYICghGhomHxYXIjEiJSkrLi4uHSAzODMuNyktMCsBCgoKDg0OGxAQGy4mICUtLTAyLy0vLS0tLy0tLS0tLS8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAABQYBBAcCAwj/xABDEAACAgECAwUFBQQIBAcAAAABAgADEQQSBSExBhNBUWEHIjJxgRQjQpGhUnKSsTNTYmNzgqKyFcHS8CQ0Q4OjwtH/xAAaAQEAAgMBAAAAAAAAAAAAAAAABAUCAwYB/8QAMhEAAgEDAgMGBQQCAwAAAAAAAAECAxEhBDESQVEFYXGBkaETIrHR8BQyweEVQlKS8f/aAAwDAQACEQMRAD8A7jERAEREAREQBERAEREAREQBERAERMGAZiYzMwBERAEREAREQBERAEREAREQBERAEREAREQBERAERMGAZieGYDmeglX4z270em3hWN9i9a6BvIbwVmHuqfmZ6k3hHkpKKu3ZFqzKvr+3mgpba1jPjq1VVtig9MF61K59MzmHGO2mp1hP2iq9KueKUT7vb/esDutPpyU+R6zTo44hIA9w9ArgoeXkGx+km0dGpq85W7ufvZe5VartKVN2pQ4rbvZeX3wdi03bbh1iF11dIC8yGbaw+atg/pIvV+0fSjlQl156ZVNq/wAdhXI9VBnOH1KW4DBTjpnw+UsfZ3szZq8MpNVHjbj3nHlVkdP7Z5eWes2T0VKkuKc8d34zTT7T1Fd8FKlZ9W8LveETS9stZqGNej09bWYzguzBc9DYRtCD65PgDLjwpdQKl+1NW1v4jUrKnyUOzHl5k8/IT5cJ0en0yCrThVUeAOSx8WYk5Zj4k5JkmDIE3Fv5VZFvShOK+eV34Jei+7ZmIiYG0REQBERAEREAREQBERAEREAREQBERAEREASM41xavSV95aT1CqqjLWOeiIvif0AyTgAkSTNic5bWfbb21Gc1jNdA8BWDhrB6uRnP7IT1zsp03OVjTXrKlDi9DU4uuo15zqmK1fh0yH3AP70j+lb0+EeR6nRs0CryUYA8pZLFkbqllxp2oYirHOa2LrfNN3+iIGyqaPEOHrYuHUESV1A5z4sJYYkslCpSpz+Ui+F6ZdOrV111bW8XoqsdTzPu2OpOOfQ7vTEsukUXDOosttPk9r7R8q1IQfQCQ9lczVeR4yNLSUuUUWMe09RhuTa6fmSYt4PogPd01KEcw1aKjqfNbEAYH1Bknwrte2kwupZraP60gtZUPDeFGbU/tAbh47uZFUs4ogYI1ignngnwn1DZmt6KlNW593I2rtbUUpKVsPk9n+dx0Cv2hcObpc58c9xqMH5Hu+c2au2ugbH/AIqtcnGHJQ58sWATl1ipX1KqPLPn5Dx+ksHA+Dam7nVpyi/1l+axjp7teO8Y/MKD5yDW0dKkvmnnyLXS9qVtRK0KV11vb3aaudO0962DcjBlPQqQR+Yn2lV4N2OSi0XtaxtHUVgVVnI/FWnOzxx3jNLVK525F2r2yIiIPRERAEREAREQBERAEREAREQBERAITtmW/wCH6zZkN9m1G3HXd3T4x65nMdBxhGoeul2Rq61IYLy2ptLbCeTYHIj1E7Hqawysp/ECPzBE4BwDjtCVDQ2I3fU3Km4KdpQp9lsDHw5jx5E48ZuozafAv9sEXVUlJfE5wu1+eCZfG1jKTVYpNq9VRSd48LF8kPPmTyIIzykTrdXaX2KiZBG/LElB157Rt34/CGP0E2G45ZZUlSkqVVVtswQSyjBFeepOMl+gzyyfhrfazVmnSstPIsO7GDzG7LM2f2sBjnzmHZk+0Jw+LqkoRitl+6VsXz+2LtjF+jtvXauWk41So/POVrZ+WN/Dd55+Zt0a46h3XS1W3ms4c1LkKfLJIyfQZnqi4ONy9MkHIIII5EEHmCD4Gfb2GcforF+lsZK3VgUBwNygYPM9Tmb3ak0/b2NLqRdWLGCkY71G7tjnzKmr8vWWWk7QnOoozsk+nsR+1OxaVClKVJtuO9+ebPba30RGtI6nhq36zT0vZcld1hR9hHP3WIHvA7clQMj+csNmkG3Mi9MVXVaZ3YKqXozMegGcZZuijn1OBJuqalQk10Kvs6DhqYJ835HTE0ei4TpmNdQRAAMAbntc4AXJ953Y4Ayf0lD1T122d5ZoLdOhOWOn1AJYHqXp2BQRnJKHcfAnlLBxzWjVawJnNenyB5Ncw5v67VO0H1ebppR1BXBBGQR4g+IlTSpJJSk2m+mMHTaiu5Nwik0t7q+enl9SZ7P8M0ldavo602uAwsHMuPAl2yzH5mTAE55RffoWLaf36ycvSTgHPxNUx+Bz1x8JPXBJaXXhHE6tTWLKmyOYIIwyMOqsv4WHlI9WnKDz6kujWjUWOXLoSERE1m4REQBERAEREAREQBERAEREAREQBExmMwCM7R6xtPpb7kKhqqrLAWGVBRSwyARkcumROVJ2Y12q1tyLbTXQ9yatgpLEbwhLrkD3XevOwnkQPmes8Y0A1FTVEld2CCOeGUhlODyIDAHB5HpIngesq07DTW1JprScLtAFeoIHxVN4nA+BveXGOYAJd47ilarhFunsepkucKfdsWmxgyHmCTWpUN4EeYPLBEr/AGl0pcVhcEBmLrzFmGqevKVvgsRv3Y6nAxO7sgM+eooR1K2KrLjmGAIx45BkyWtnKHBLOLFXDsqjTqqrDDTv3eh+deM8C4bZpqbaVvGrZwbqdlm4/trtx7vPxEkNJwyoalbEp7kKuKqwe87hSSTkBsvcxY+QA8Z19+z+hRWtZEFQG4hnJqVR1bYT3YGPTHKVuztPpr7Ero7rYbq6RSUTN9Vm5WuAI/oxhgAOZKnPUCRIpRd03fltjww8979CyrOVZNStl53vLN+qsu5ebIUaVN/eFXGwFUNvxndjexA5IDgAKMYAJ8ZAcW4l3B3KpJwxB6KuAT7zeGeg8ycSX7RapNPddUvwraErUZJyyI3dqBzJDswCjp08JE3cIaw3V6tCjYFYTdk1h0D7228u898cueMfOXGmiqdCNODfE1e7y+rbf50RyupTlXlVqx+SDSxheCt06Lb0PO5qaUpGQ122j3cDG/8ApXGOmF3nlLjTxbY9NNW3GCXH7FKqVXGOhLFAB6N5SiNa9V1Q1JrwFcK4b4m91cspHufFjOSMnGeck+DanLX2ZHxlAc/+nUv/AFlzNs6cajttyt0SVzCFaVFcTynd3Wzblb7+eGky+m9LDtDDOM4yM46Zx1x6yMr0L6ex79KdtzEHn8LgADun/sHB59VLEjyMZ2bu3k34wbAAvmKVJNY+uWb/ADYk5xDWKoIz7wAb6HIH57TNDp3fByZNjqOFOonlblz4FxVNXQl9YIDjmp6o45OjY/ErAg/KSUpXsy1G+vVDoF1T4H+JXTa35vYx+susqpR4ZOPQv6c+OCkuaT9RERMTMREQBERAEREAREQBERAEwZmafFtT3NFtmM93W7489qlsfpAKV9rOue5rTcKlsZK0yyIyISu7CkGzJBOW5dMDxmhZQaWJ0tj0Hr92x2n95GyjfUZn11VV1NFa1FMoqqQ4b3sKB1U5ByOuDK1ZrtauS1VT/uWf8nUfzlpRpRSyr+RRamvNy+WVn42+uC0cN9oViOKdXQXsYla3oGBY2MhWR29zkCd2SvInl0k1RxwWt3OvoqVLTtUhzYhJ6JZvRdpPgeYzyyCRmg9jgdTbbfYhRq/uQrY5OQGsPIkHlsAPzmz2v14pVQzHDEqy4+JSpHM+GOR+k1S09N3cduRIp6usuFTs3zOhjgltP/k9QyDwquBtrH7uSLF69A+BjkJo26DiFlpOpXT20rjZUlj1gkYO61WRu8ORyG4KPEE85M6DUdzpK31VgUpShtdiAAwQb2J6DnmVLtF2zvZG+xoa1I5XWD3sH8VdRHL0L+P4SOsSFOU3aKLCrVhSjxTdkb3fodT3f2Srvsd4yC8EKByWyxFUrk/CGIz5csze7TG5dO50aoLACSdvPZg7u7AHN8dM8s+fQ1z2PcC7ui7VOSz6u1nDsclqlJCEk9cks2fHInQXoGJ4rJnuZLBwOrRWd4LartjBNoIZhu3HLFnVgwJ5cwQeucze1Dbu6PfivUBErsOpZzRqCuQGXUcylmCB94OeB5EzY7b6WzS3WCkDaCLVXOM1PnKg+YKuAPLHlIjQXWOjNT96GJzW+M9feTJ5cjnkR18ZbOnTqWnDErXx+Ztzt6ZOd+JWpXp1bSje2fHDvsm/3X55yT//ABM6DvtPrtCSdWpUObE7t6tmBWr+JBZmx15k+Epxp7uo1U2J7wBesc8gAd53WDlSQD1z9JPNxZqtFdUK++05rdTprBzpbacNXuBKlcg7emANuPHxwQA0VkDqg8vLry/79TMdNQfHNT3eb9V3dD3WaqCowlT/AGxduFrKayr9e5rxTyWLhFysC1ZXmvunBK58MgEcvTlIOnVq9moCObPvFLNnOXFaI+McgoZcAfOe7dFWxJK8z1wWXd+9tI3fXM816R7nr01XI2MKwBy2Kfjbl0CqGP5eclTg4v4r5fb29yFp61OpH9Or/M/568/JI6T7N9Nt0KP43s9x+Tn3P9CoJbJraPTJTWldYCoiqigdFVQFUD5ACbM59tt3Z2EYqKSXIRETwyEREAREQBERAEREAREQBIPtm+3RXeqhfozKp/QyckN2u0bX6LUVp8RrYr6so3KPqQBB49ince4iKyVZLfPctbOOvTK5OfpKtquLDHu1XN/7Lj/cBLFxvi6AA7LSHAYMtbMuG59Vz4Hxlfu4kHGKqrW9WXaoOPFnxy+WT6S7oySjv7HLamlJ1L8N1429/wCza7EX3WV39zpmfu7m7wB0DkthgQjEZwuB8XhylZ7Zav7ZYO4cH3NqdRtd8q5bxG1Qw+bY6ib/AAHVvT9prFgQ24NxUH36m+HY2cqQBYmfI55HGPpwGr7ThjtAPMAfsZIT/TiaYUpSk1N4JlbUQgoumryaXPF3tvve3p37b2j7RW8TKJrNoTS43ID7t1oHK+wHlj9lOgIJ8seO1XHFsCabT+/bqXWlCoyFLkKWz0JGScfnN7VcDpRbbH27CELZ6YQNzbPIjLfoJ9uyXZ/dqNLqb1ILNbbQhyNtVale8YftMbK9oPQep5YTcaNOyw/c3UuOvVTllc+iwseu2x07hejWiqupBhK0VFA8FUBR+gm4ZhRPUrS3Rz/2l6IfcW4/E9Tfuuu8Z+RrwP3jOeMn2Jjeg+762qPDw71B5gdR4gZ6jn1f2jJnRlv2LdO3/wAyKf0YznGoG7cCDgcufRgRzx/KXOhfHScXunjzOY7YXw9QpcpLK62/F4Hxv1K3MLKtpDDa2DyZfA/MevgfQT1wnT91WEAwFJA9UzkfLkZX+HcPsp+8Rm3hypWxiVtqU4UAnoduMHp4dOlh0mrWwcuTD4kPJ1+Y8vXpJdB8VnJWdvLPT+fEr9XDhTjB8UbrPPG17dz3WPQ2LDyPPHI8/L15yy+y7hTMX1lmWBHdUMR1QH7ywDOAGIABGMhc9DKPrz3h7kHw3Pg8wnQJ6Fuf0B9JNcH1l+kwdPay4x7jMzoQOQUox5DHipBmrW0p1lany8c9y5epJ7M1FLSPiq3zthYXW+/p9js2YzKlou3NBrB1GarOQKhWcMfOsqPeHzwR4iebO3VZOKqLG9WKIv8AuLf6ZSqjUbtwv0OneroJJ8as9slvzGZTV7V3sf6KhR/iOx+o2KP1mpqu1mpQhe8oLt8NaUWu7fuotuT6nGB4w6FRK7QjqqMnaMrvuL7mZlf7K6jX2Kza9KkBx3aqCHx494u91U+gYywTUSBERAEREAREQBERAEwZmIBzjtFwu/SkmupraCSV7sFmpBOSjIMllBJ2lQcDkR7uTX7hrLl+40WofI5EpsH527Z2YiYCyVDV1IR4UQavZ1CpPiktzhul9n/F7a3ayumtrGGa2tO4VgY27kDAeJzk9T0m3wzspxbSMCdOligdKrk6AdB3m3/vznaJGce4vVo6jbccDkoA+J3bkqIPFiZgtTVvubJaOi/9fy1io6XhxLd/xBBTpaV37bWX37MqUZlUkbVwcKeZYjl7oz77O9rk13E3RK3RK9Oe7ZwVNubELsqkZUcl5Hn8pXOLavVam3vNQVK49yoZ20tnlgfjfGQXPlyABOY+jWtpbk1CDJrOSB+NCMOnpkdPUKfCS/0c6lN1Jfu6Fd/lKNOrGhTV49fz+TuIgyN4LxenVUpdQ4etxkEeHmCOoYeIPMTdNwldYurlY9obj7I6nq70KPpajn9FY/Scz1+vCZwMn1IAHluY9PlzPpJzt32jS9/cbNVBKAjBFlxwhI8wuSoI8S/lIQUBjuI5+Hp8vX1l1oaco0sbv6dfsct2tWpz1C4ldRx4vd/VEZpeKLZZ3fQlSw55GQeYDDkeRB8CPESQs0iWjDj5FSQw+TDmJE9o9IVAtpAFiZYHzwDlWHiCN3yMl+B9nuL6pFP2WukMFPe2ONu0jO4IuWPLwmx6hU7wreWMNGEdHKvGNTTY6q6un/ZmiquoYUY8fEk+pJ5kz6LrUPQy98B9nNFXv6tzqbPJhiofu1Dr/mLTf4l2A0NoOyruGP4qMJg+ezGw/VTNH+TgnZRwSH2DOS4pz+bz+v8ARz5XBnyv1IQEk4A8Tyk1r+wetqONO1dynkCzGsr6sMEEeZXn5LLDwD2f00sLdUx1FowQGGKkIOcpX4nPixJ8sTbU7RpqN45foRqPYVaU7TaS9Ss8A7OarWkNzpp694w95x/dof8Ac3LmCA06RwfgdGkXFKAE/E55u582c8zJMRKitXnWleR0mm0dLTRtTXnz/O4zERNJKEREAREQBERAEREAREQBERAMGUDtLamq1a+KaXegPLDah8b9vmUVduR4s48DL805Ndr9NXY+ktes2VvYFGRlkZmZWUjxKsAcHOQczfp0nUImtlw0n05+Bpcd4zTUdu4M37Kncc9MYXJB9JEanSW2KXsG0dQn/Xjqf7I5efkJ/UahQuKlQY5AYwOXhy6flIDW8X1VSlm09LAczttbIA6nBUbuXgDLh8UVeV7dxzkalOTtTte/NrPht65feamjos04Nql62b3nzY65bwzsIAwOXIdeXhmSWh1uo1lRdKNZcnNelro2P2SxKsPWfbs7p01GtSjiB7yq0HugnuIbAN3d2DmTkA45gHGCDkCdspqVFCooVVGAAAAAOgAHQSBWr/ClaMFjqlkttPpP1FPinN2f/FtLHLvPz1abu9CW0W0qtRsC21lM8yo2gjoMfykpwk5pqPnXWfzUGWH2nHOsA/Z0383s/wDyRnZHS95pNO3nVX+igf8AKT9NWvBTlu7/AFsVHaGmaqOlT2VvdXIniFb7SXI+OsgAclUMMgn8Wec6z7PdRv0FA/qw1Py7pig/0gTm3aSjYjH5fzEuPsp1m5NTSTzrtVwPJbEH/wBkcyN2gk4pru/kn9juUZuMvy1vuX0TMRKk6AxMxEAREQBERAEREAREQBERAEREAREj+M1M1Lhbu45ZNoCkoo5sw38gcZ5nOOsAje0/bDR8OAGotUO3NawRub1wSAo9WIEqdPbjWcQyvDKtwG4b1rLIrfh3X3FFBz1Co/oZB6Xshwq2z7XadRfWvvszd7Y1/k9pRdtacshScnx24wb5pdRqdSiroaxpNOFAW22v3yvL+h03IKP7Vnj+Ejri2CrUrqLt66257HrY1ttsbumJUF1CIqKygnbghuYPMyv8S7NozjYqoo57VRQM+fTrLP2m7L6Hh2kUqu617qh3tzl3Lb+8cqWOFYhX+EDrIKzV55n85caGMatN42Oc7UrT09RWbbd/L1ur+BDDg91RxVqG2+Icqx+jY/mJJ6Ogjk7bs+Y/MknOZ8U4mrtsqDWNkDbWjORnpkIDiTWn7Pa+zBXTWKD0Lsi/mC24flJnxKFL/b3Kx0tZXjbgfja1/OyIzW6VfHB5gj0PgfQzovs54pbqNKwuJZqbWp3HqyhUdSx8ThwM+OM+MrNXYDXW/HbTSOfTdafTkNg/WXzs9wWrQ0imkHGSzMebWOfidj5nA9AAAMACVuur0qllDdcy87K0deg5OphPle+Sh+0bSvXqxe4zTdXXSrDoliG0lX8t28YPTKkdcZieymrGlXuGJIGTW392MDafUfrn6Sf9uGqJ0lekQ4fU2ZHolI7xj/FsH+aUDgesRa1XVXIjKAN75AdDzVgT44OCPMTLRz4ocM8Jc/qjDtGm6dT4lPLdrx9k/wCGSXabWrc497Fdf3jnpkrzAP8AZ5En5Y8THsU7XBtffp2AA1IDVnx3VBvd+qkn6SA7Uaiq5O601yWbs72TnsrUbjn59AJraTT/AGa/S3oAo0hrLHHN1XZ3hPqPvfoJ7qk5q1PKWfH/AMR7oGqb4quG8eHX/s/Y/TwmZ5U5E9SsLwREQBERAEREAREQBERAEREAREQBPLDPIz1EAheL8CXUujNdcq19K0YBCeu4jaSWGBg593qMGNN2cpQc31D/AOJqdQ/6M+JNRAIrV9n9HcALtNTbjp3laPj6uDNG3sVw5uR0lQH7KrtU/NFwpHpiWOIWNjxq+5qaHh9NC7KKkqQfhrRVH5KAJtATMQeiIiAcn7f1m/ie09KNPXt9Da1m79EX8hIkcH3+UmuPX7tfqs/hetB6gU1N/Nmkhw+gES600vh0Fc5rWw+Lqn3fwVNOzmz4VUDrgKB/Ka2s0O3qPSdEOmErnaNAik7WY8gFUZZj5AeJm6lqFsyNqNHNZje/qXL2fcQN+hryctVmliTk5r5Ak+ZXafrLNOaexXiC3V6wIcqLkYH96pAf9gnS5RVElN22uzqqLk6cXLeyv6CIiYGwREQBERAEREAREQBERAEREAREQBERAEREAREQBETBgHKeEcI+2a3XPcG7qi23cuSN9pzsXIOcKgRj57k8jILsR2lL0KXJJGVJJ5nacc/XGJ0yhhXRr3x0s1LH6IB/ICfnTsZxNK0dHYDnvGT1GOeP4ZM0dXiq2nta3sVnaFFxoOVNZTv67nXuLcZvp0660BTpu+FDDHMJkobw3kLBt245gZzNzs3eL9fTn8C22D5hRXn8rTJPXcG38CfT9SdGSPWzu+8B/jnNvY9xS99ULrK2+z11jTNb+FbbCgXJPXcVUcs43AnAM1fqL0p9+3qb/wBLapBrlv6Ft9nKLoeK8S4fjaHYaqr1rPVR6DvFA8eRnUpzTtJpGq7Q8OvrH9NVbTZ8kDNn54cfwzpcjrYmCIiegREQBERAEREAREQBERAEREAREQBERAEREAREQBERAKfx2zutLxXl8KW2j1D6cEn+JXkP7J+ytQ4OlepqVxqd1zqy5yHwE69DsC/nLB2n4RZe+xEzXqk+z6g5A2Vqd4bzOVa1OXPLqegMsdVYUBVGAAAAOgA5ACeJWBE8EYtpu7fm9Yah/wB6v3MkeGQA3yYechfZfoFHCKanUFSLVYH8QNlgOfmJLcTtGkta9iBVau2w9AlqjFbn0Ye4T5iufTsbQ1eg0quNrdzWWHk7KGYfmTPIqwIumljrtPTbln06aixLCD95UwrrUlsY3jcQR1ON3jLfMYmZkBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAPjqKFsVkdQysCrKwBDA8iCD1E9quOQ6T3EAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREA//Z"
    )
    monsters.append(m2)

    m3 = Monster(
        name="EarthyPlant",
        type="Leaf",
        health=20,
        image="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBIWFRIWFBEYGBQRERgSFBgSFRIRFRESGRUZGhcUGhgdJC4nHB4rHxgcNEYnOC8xQzU1HSQ7QDszTTw0NTEBDAwMEA8QHhISHzQhIyE0NDExNDE0NDE0NDExNDQ0NDExNDQxPzExMTE0NDExNDQ0NDQxNTQ0NDUxNDQ/Nz8/NP/AABEIAOEA4QMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABAUBAgMGB//EAD0QAAICAQMCBAQDBQYFBQAAAAECAAMRBBIhBTETIkFRBjJhcVKBkRQzQmJyFSM0gpKhFnOxstEkU2STov/EABgBAQEBAQEAAAAAAAAAAAAAAAABAgME/8QAIREBAQACAgICAwEAAAAAAAAAAAECESExA0ESUSJCYRP/2gAMAwEAAhEDEQA/APs0REBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERARExmBmYlXrutU1ts3brTwEQruz6ZJIVfzIleeoWsT4zNpk7eQV2Y+r3ZZV+21cZ7mS2TselmJUWaK9eatU+4fw3qlqN9DtCsPuG/IzppOoEsK7k8O4jKjdvS0Dkmt+N2PYgEe2OSllFpERKEREBERAREQEREBERAREQEREBERAREQERMQMxNGcAEk4A9T6Sj6l8T6evypYt17nbXTS6NY7+gPOFX3Y4Ak2LPqGvqpRrLbFRFxksdoyTgAe5J4A9TKbUau+zlq7K9O4OBWC2of084XzVKQewy3uU7TjpdFY7C7VMr3clEUE06UEEEVg/M2DguRk84CjiTK9O1eXqGPVqxgLYPXaOyv7H17H3HK+SW6gj6AELsp2PSCQUsXze5VnH8X9Skn1PrN6CqchdtTHYVYYOnt7GtvQIcjHpyMcMMS9aVKDU18lUDkqP3tPdlI9SBkj2I+pzyd1DjIBr1P93YDypYqdrY9cgbT7jb7SWa4t3sdum3bG8E9gCaT/KMZr+65/049jJeq0yWKVYZGQwxwVYHKsp7qwPIMrtLobRYm8gpTu2NuJezcCqhhjjCk5OTkgHjmSR1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cRjfuYsSWH5Z+0zr9RZfUq2aXcjMr76XV2rdSCG2OFOQwIK/cSP0x7ay5rpe6ywYL2D9kqQA+VVRyXxkkk45/TE3Nc1qXH43fa96d0PTafcaKVQuecFjgZztXJO1c+gwPpOfS9OjX6nUBQS5SlX4O5a1IYg+25mH+U/SRtFTqdQGN9irVuKrXptyi1QAGLWN5iu7Pyhcj3B5n6wny6aghCUG5kAH7PR2BUdgxxhfbBPOMG47rO1H1fS3aizUJpGCgFGssLOqG+tvNQCvJLKqqxHy49TxN/gv4at05ey9l3sGRFR7LFqQuSTufuxAUHgfIPcz1Ol0qVqqIoVUGAB6D/z9ZInSSTpGBMxE0NSoPBHE0WlRyEUH6ACdYgIiIGCJ5/U/C9O5n07NprGbcxoICO3GS9TAoxPvgH6z0MSWbFHotBqBcr2PWwWtq2ZFsrNgLBlBQkgYIPO4/MwxzLyIiTQREShERAREQEREBERATEEyHqOoVItjFwRVwwQ7mDE4CYHO4ngD1MCHrxv1GmrXg151DsMblQeVUB7jcx59wjS1IlL0Ql3vufy2WBE8IjD6etNxRWPqSXY5HHOATjJuS05Z5RYqNXQUZnVSUY7nVVLFH9XVRyQfUDPPPvnilZt8qbvDPzuVavcvqqZAJJ/EOAM4Oe12YnCyb2aK1AAAGAAAAOAAOwkChgNZco/i0tLn8nuUf7SwWVWpIr1SWscV3Urpg3otosZkDewbcQD74HqJ38ZV3ExMzqhERAREQEREBERAREQEREBERAREQEREBERAidQZxVYUIDitipbsHCnaT34z9DPltOq2FbAWU1FWqS9axY27LEWBOHXz5DdwTnuJ9blZd0DRspVtLUVJ3Y8NPm984zmFefXrNWyvU+IiFSA4Z6wdm/bZWRnkggkfVR7y7/tlTzVTdcoOC1SAJ91Zyu8f07pN0/TaEChKK1CDC7URdoHtgSZOU8UnfKdKcdar/irvU+zabUnH5qhH+80f4k0a/PqFT/mB6/8AuAl3E1/niu1boeqae7cKb0cpjcEdWKg5xnHpwf0kLqNguL1MM0L5LR/7rY5r/pGefc8ehzO13R6bCGKbbFJK2Vk12ITjOHHODgZByDjkGVo6RqUUrXdW+NxQ3oytuJJy7ocNye+0HvMZYWT8Upo+u11Kar7GNlLbPlax7KtoZLmCgnBVgC34gZe6e9HVXRgyuoZWUgqynsQZ861Xwjr9QGy1dGSNxs3XvewyCzbSAB7DtjjAHf3XROn+BRVTu3eGm1nwF3uTln2jgZYk49J1m9ciyiIlCIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiBjEzEQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQP/Z"
    )
    monsters.append(m3)

    m4 = Monster(
        name="WaterDevil",
        type="Water",
        health=20,
        image="data:image/jpeg;base64,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",
        user_id=1
    )
    monsters.append(m4)

    m5 = Monster(
        name="FireDino",
        type="Fire",
        health=20,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzkOuDkFlUlmT6189ICgM40mKiY-uvj3khNQ&usqp=CAU",
        user_id =20
    )
    monsters.append(m5)

    m6 = Monster(
        name="FireDino",
        type="Fire",
        health=20,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzkOuDkFlUlmT6189ICgM40mKiY-uvj3khNQ&usqp=CAU",
        user_id =19
    )
    monsters.append(m6)

    m7 = Monster(
        name="FireDino",
        type="Fire",
        health=20,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzkOuDkFlUlmT6189ICgM40mKiY-uvj3khNQ&usqp=CAU",
        user_id =18
    )
    monsters.append(m7)

    m8 = Monster(
        name="FireDino",
        type="Fire",
        health=20,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzkOuDkFlUlmT6189ICgM40mKiY-uvj3khNQ&usqp=CAU",
        user_id =17
    )
    monsters.append(m8)

    m9 = Monster(
        name="FireDino",
        type="Fire",
        health=20,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzkOuDkFlUlmT6189ICgM40mKiY-uvj3khNQ&usqp=CAU",
        user_id =16
    )
    monsters.append(m9)

    return monsters

def create_moves():
    moves = []

    m1 = Move(
        name="Fire Throw",
        type="Fire",
        damage=7,
        accuracy=.1
    )
    moves.append(m1)

    m2 = Move(
        name="Water Throw",
        type="Water",
        damage=7,
        accuracy=.1
    )
    moves.append(m2)
    
    m3 = Move(
        name="Leaf Throw",
        type="Leaf",
        damage=7,
        accuracy=.1
    )
    moves.append(m3)

    m4 = Move(
        name="Cut",
        type="Leaf",
        damage=3,
        accuracy=.3
    )
    moves.append(m4)

    return moves

def create_monster_moves():
    monster_moves = []

    mm1 = Monster_Move(
        monster_id=1,
        move_id=1
    )
    monster_moves.append(mm1)

    mm12 = Monster_Move(
        monster_id=1,
        move_id=4
    )
    monster_moves.append(mm12)   

    mm2 = Monster_Move(
        monster_id=2,
        move_id=2
    )
    monster_moves.append(mm2)

    mm22 = Monster_Move(
        monster_id=2,
        move_id=4
    )
    monster_moves.append(mm22)

    mm3 = Monster_Move(
        monster_id=3,
        move_id=3
    )
    monster_moves.append(mm3)

    mm32 = Monster_Move(
        monster_id=3,
        move_id=4
    )
    monster_moves.append(mm32)

    mm4 = Monster_Move(
        monster_id=4,
        move_id=2
    )
    monster_moves.append(mm4)

    mm42 = Monster_Move(
        monster_id=4,
        move_id=4
    )
    monster_moves.append(mm42)

    mm5 = Monster_Move(
        monster_id=5,
        move_id=1
    )
    monster_moves.append(mm5)

    mm52 = Monster_Move(
        monster_id=5,
        move_id=4
    )
    monster_moves.append(mm52)

    mm6 = Monster_Move(
        monster_id=6,
        move_id=1
    )
    monster_moves.append(mm6)

    mm62 = Monster_Move(
        monster_id=6,
        move_id=4
    )
    monster_moves.append(mm62)

    mm7 = Monster_Move(
        monster_id=7,
        move_id=1
    )
    monster_moves.append(mm7)

    mm72 = Monster_Move(
        monster_id=7,
        move_id=4
    )
    monster_moves.append(mm72)

    mm8 = Monster_Move(
        monster_id=8,
        move_id=1
    )
    monster_moves.append(mm8)

    mm82 = Monster_Move(
        monster_id=8,
        move_id=4
    )
    monster_moves.append(mm82)

    mm9 = Monster_Move(
        monster_id=9,
        move_id=1
    )
    monster_moves.append(mm9)

    mm92 = Monster_Move(
        monster_id=9,
        move_id=4
    )
    monster_moves.append(mm92)

    return monster_moves

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        print("Clearing db...")
        User.query.delete()
        Battle.query.delete()
        Monster.query.delete()
        Move.query.delete()
        # Battle_User.query.delete()
        Monster_Move.query.delete()

        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        # print("Seeding battles...")
        # battles = create_battles()
        # db.session.add_all(battles)
        # db.commit()

        print("Seeding monsters...")
        monsters = create_monsters()
        db.session.add_all(monsters)
        db.session.commit()

        print("Seeding moves...")
        moves = create_moves()
        db.session.add_all(moves)
        db.session.commit()

        print("Seeding monster_moves...")
        monster_moves = create_monster_moves()
        db.session.add_all(monster_moves)
        db.session.commit()