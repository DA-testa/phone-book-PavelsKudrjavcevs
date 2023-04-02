# python3
# Pāvels Kudrjavcevs 2.grupa 221RDB353

class Query:
    def __init__(self, query):
        self.type, self.number = query[0], int(query[1])
        self.name = query[2] if self.type == 'add' else None

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print(*result, sep='\n')

def process_queries(queries):
    contacts = {}
    result = []
    for query in queries:
        if query.type == 'add':
            contacts[query.number] = query.name
        elif query.type == 'del':
            contacts.pop(query.number, None)
        else:
            result.append(contacts.get(query.number, 'not found\n').strip())
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries())) 


