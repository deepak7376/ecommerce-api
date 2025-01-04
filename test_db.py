import psycopg2


def main():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_lbga2-fK-231MnbnDno@pg-375da4cf-dky-54ea.b.aivencloud.com:16211/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()