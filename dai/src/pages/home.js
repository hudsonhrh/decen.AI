import React from 'react';
import {
  Box,
  Heading,
  Text,
  Button,
  VStack,
  Container,
} from '@chakra-ui/react';



const Home = () => {
  return (
    <VStack spacing={10}>
      <Box bg="purple.600" w="100%" py={20}>
        <Container centerContent>
          <Heading as="h1" size="4xl" color="white">
            Decen.AI
          </Heading>
          <Text fontSize="2xl" color="white" mt={10}>
            Deploy a fully Decentralized AI Agent
          </Text>
          <Button colorScheme="whiteAlpha" mt={10}>
            Deploy Now
          </Button>
        </Container>
      </Box>
    </VStack>
  );
};

export default Home;